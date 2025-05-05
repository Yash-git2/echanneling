from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, AppointmentForm
from .models import Appointment
from .models import LabTestBooking
from .models import Doctor
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
    appointments = Appointment.objects.filter(user=request.user)
    lab_tests = LabTestBooking.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {
        'appointments': appointments,
        'lab_tests': lab_tests,
    })

@login_required
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, user=request.user)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, "Appointment cancelled successfully.")
        return redirect('dashboard')


# Doctor appointments view
def view_appointments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        appointment = Appointment.objects.create(
            user=request.user,  
            name=name,
            date=date,
            time=time
        )
        messages.success(request, f"Appointment for {name} on {date} at {time} has been successfully booked!")
    appointments = Appointment.objects.filter(user=request.user).order_by('-date')

    return render(request, 'dashboard.html', {'appointments': appointments})

def book_appointment_view(request):
    # Any logic for booking an appointment here (if any)
    return render(request, 'appointment_booking.html')  # Use the correct template name

def emergency_numbers(request):
    return render(request, 'emergency_numbers.html')

@login_required
def lab__test(request):
    if request.method == 'POST':
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        test = request.POST.get('test')
        preferred_date = request.POST.get('date') or None
        preferred_time = request.POST.get('time')
        prescription = request.FILES.get('prescription')
        notes = request.POST.get('notes')

        LabTestBooking.objects.create(
            user=request.user,
            full_name=full_name,
            email=email,
            test=test,
            preferred_date=preferred_date,
            preferred_time=preferred_time,
            prescription=prescription,
            notes=notes
        )
        messages.success(request, "Lab test booked successfully.")
        return redirect('dashboard')  # Assuming this exists in your urls.py

    return render(request, 'book_lab_test.html')  # Use a dedicated template for lab test booking
        

# Lab test appointments view
def view_lab_tests(request):
    lab_tests = LabTestBooking.objects.filter(user=request.user).order_by('-preferred_date')
    return render(request, 'dashboard.html', {'lab_tests': lab_tests})

@login_required
def reschedule_appointment(request, appointment_id):
    return redirect('book_appointment')



def doctor_list(request):
    specialty = request.GET.get('specialty')
    sort_by = request.GET.get('sort')

    doctors = Doctor.objects.all()

    if specialty:
        doctors = doctors.filter(specialty__icontains=specialty)
    if sort_by == 'available':
        doctors = doctors.order_by('-availability')

    return render(request, 'doctor_list.html', {'doctors': doctors})

def doctor_profile(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    return render(request, 'doctor_profile.html', {'doctor': doctor})


def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            
            # Simulate payment (For now, mock the online payment logic)
            if appointment.payment_method == 'online':
                appointment.is_paid = True  # Assume payment is successful for now
                
            appointment.save()
            return redirect('appointment_success')  # Redirect to success page or another view
    else:
        form = AppointmentForm()
    return render(request, 'appointment_form.html', {'form': form})