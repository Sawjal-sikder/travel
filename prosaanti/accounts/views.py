from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            username = User.objects.get(email=email).username
        except ObjectDoesNotExist:
            messages.error(request, 'This email is not registered. Please check your email or create an account.')
            return redirect('signin')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful! Welcome back.')
            return redirect('home')

        messages.error(request, 'Incorrect password. Please try again.')
        return redirect('signin')

    return render(request, 'signin.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        password = request.POST.get('password', '').strip()
        cpassword = request.POST.get('cpassword', '').strip()

        # Check if any field is blank
        if not email or not phone or not password or not cpassword:
            messages.error(request, "All fields are required.")
            return redirect('signup')

        # Check if passwords match
        if password != cpassword:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        # Check if email is already registered
        if User.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered.")
            return redirect('signup')

        # Create the user
        user = User(username=email, email=email)
        user.set_password(password)
        user.save()
        messages.success(request, "Registration successful! Please log in.")
        return redirect('signin')

    return render(request, 'signup.html')


def signout(request):
    logout(request)
    return redirect("signin")
