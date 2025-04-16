from django.shortcuts import render, redirect, get_object_or_404
from .forms import AppointmentForm
from .models import Appointment
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

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
                return redirect('dashboard')
            else:
                form.add_error(None, "This slot is already booked.")
    else:
        form = AppointmentForm()
    return render(request, 'appointment_booking.html', {'form': form})

#@login_required
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

from django.shortcuts import render

def book_appointment_view(request):
    # Any logic for booking an appointment here (if any)
    return render(request, 'appointment_booking.html')  # Use the correct template name

# Create your views here.
