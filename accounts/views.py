from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from contacts.models import Contact

def login(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')

def register(request: HttpRequest):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists!')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    first_name=firstname, last_name=lastname,
                    username=username, email=email, password=password
                    )
                user.save()
                messages.success(request, 'You are registered successfully!')
                return redirect('login')
                
                
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    return render(request, 'accounts/register.html')

@login_required
def dashboard(request: HttpRequest):
    user_inquiry = Contact.objects.order_by('-created_at').filter(user_id=request.user.id)
    context = {
        'inquiries': user_inquiry,
    }
    return render(request, 'accounts/dashboard.html', context)

def logout(request: HttpRequest):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are successfully logged out!')
        return redirect('login')
    else:
        return redirect('home')