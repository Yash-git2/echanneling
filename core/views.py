from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, AppointmentForm
from .models import Appointment
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            # Check if slot is available
            exists = Appointment.objects.filter(
                doctor=appointment.doctor,
                date=appointment.date,
                time_slot=appointment.time_slot
            ).exists()
            if not exists:
                appointment.save()
                messages.success(request, "Appointment successfully booked!")
                return redirect('dashboard')
            else:
                form.add_error(None, "This slot is already booked.")
    else:
        form = AppointmentForm()
    return render(request, 'appointment_booking.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.is_authenticated:
        appointments = Appointment.objects.filter(user=request.user)
    else:
        appointments = []  # or None or some default data
    return render(request, 'dashboard.html', {'appointments': appointments})

@login_required
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, user=request.user)
    if request.method == 'POST':
        appointment.delete()
        return redirect('dashboard')

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

def view_appointments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        messages.success(request, f"Appointment for {name} on {date} at {time} has been successfully booked!")
    return render(request, 'appointment.html')

def emergency_numbers(request):
    return render(request, 'emergency_numbers.html')

def lab__test(request):
    return render(request, 'book_lab_test.html')

