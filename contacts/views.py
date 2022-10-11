from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User


from car_market.settings import DEFAULT_FROM_EMAIL

from .models import Contact

def inquiry(request: HttpRequest):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        customer_need = request.POST['customer_need']
        message = request.POST['message']
        
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                car_id=car_id, user_id=user_id
            )
            if has_contacted:
                messages.error(request, 'You have already made an inquiry about this car. Please wait until we get back to you.')
                return redirect(f"/cars/{car_id}")
        
        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id,
                          first_name=first_name, last_name=last_name, email=email,
                          phone=phone, customer_need=customer_need,
                          message=message
                          )
        admin_info = User.objects.get(is_superuser=True)
        send_mail(
            'New Car Inquiry',
            f'''You have a new inquiry for the car {car_title}. Please login to your admin pane for more info.''',
            DEFAULT_FROM_EMAIL,
            [admin_info.email],
            fail_silently=False,
        )
        contact.save()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly!')
    return redirect(f'/cars/{car_id}')