from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after signup
            return redirect('home')  # Redirect to homepage
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Ensure this matches your URL pattern
        else:
            messages.error(request, "Invalid username or password")  # Show error message
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})