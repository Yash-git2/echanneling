from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')  
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        messages.success(request, f"Appointment for {name} on {date} at {time} has been successfully booked!")
    return render(request, 'appointment.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
