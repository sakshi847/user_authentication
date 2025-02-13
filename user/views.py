from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import SignUpForm, LoginForm, PasswordResetForm
from .models import User
from django.core.mail import send_mail
import random
from django.contrib.auth.decorators import login_required


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect("dashboard")  
    else:
        form = SignUpForm()
    return render(request, "user/signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password) 

            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect("dashboard")  
            else:
                messages.error(request, "Invalid credentials")
    else:
        form = LoginForm()

    return render(request, "user/login.html", {"form": form})



@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'user/dashboard.html')


# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')


otp_storage = {}

def password_reset_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.filter(email=email).first()
            if user:
                otp = random.randint(1000, 9999)
                otp_storage[email] = otp
                send_mail(
                    'Password Reset OTP',
                    f'Your OTP for password reset is {otp}',
                    'your_email@gmail.com',
                    [email],
                    fail_silently=False,
                )
                return redirect('password_reset_confirm', email=email)
            else:
                messages.error(request, "Email not found")
    else:
        form = PasswordResetForm()
    return render(request, 'user/password_reset.html', {'form': form})

def password_reset_confirm_view(request, email):
    if request.method == 'POST':
        otp = request.POST['otp']
        new_password = request.POST['new_password']
        if email in otp_storage and otp_storage[email] == int(otp):
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            messages.success(request, "Password reset successful!")
            return redirect('login')
        else:
            messages.error(request, "Invalid OTP")
    return render(request, 'user/password_reset_confirm.html', {'email': email})

