from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment

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
    return render(request, 'core/book_appointment.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'core/dashboard.html', {'appointments': appointments})

@login_required
def cancel_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id, user=request.user)
    appointment.delete()
    return redirect('dashboard')

# Create your views here.
