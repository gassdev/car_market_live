from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages

from cars.models import Car

from .models import Team

def home(request: HttpRequest):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_at').filter(is_featured=True)
    latest_cars = Car.objects.order_by('-created_at')
    search_fields = Car.objects.values('brand', 'model', 'year')
    
    context = {
        'teams': teams,
        'featured_cars': featured_cars,
        'latest_cars': latest_cars,
        'search_fields': search_fields,
    }
    return render(request, 'pages/home.html', context)

def about(request: HttpRequest):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'pages/about.html', context)

def services(request: HttpRequest):
    return render(request, 'pages/services.html')

def contact(request: HttpRequest):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        
        email_subject = f'You have a new message from Car Market Website regarding {subject}'
        message_body = f'Name: {name}. Email: {email}. Phone: {phone}.\nMessage: {message}'
        
        admin_info = User.objects.get(is_superuser=True)
        send_mail(
            email_subject,
            message_body,
            f"Visitor {name} <{email}>",
            [admin_info.email],
            fail_silently=False,
        )
        messages.success(request, 'Thank you for contacting us. Will get back to you shortly.')
        return redirect('contact')
        
        
        
    return render(request, 'pages/contact.html')