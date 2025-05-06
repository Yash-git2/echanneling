from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, AppointmentForm
from .models import Appointment
from .models import LabTestBooking
from .models import Doctor,DoctorAvailability
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from . import views
from .forms import RescheduleAppointmentForm
from datetime import datetime

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
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

            doctor = appointment.doctor

            # Convert selected time_slot string to a time object
            try:
                selected_time = datetime.strptime(appointment.time_slot, "%I:%M %p").time()
            except ValueError:
                form.add_error('time_slot', 'Invalid time format.')
                return render(request, 'appointment_booking.html', {'form': form})

            # Get availability record for that doctor and date
            try:
                availability = DoctorAvailability.objects.get(doctor=doctor, date=appointment.date)
            except DoctorAvailability.DoesNotExist:
                form.add_error('date', 'Doctor is not available on this date.')
                return render(request, 'appointment_booking.html', {'form': form})

            # Check if selected_time is within doctor's available range
            if not (availability.start_time <= selected_time < availability.end_time):
                form.add_error('time_slot', 'The selected time is outside the doctor\'s available hours.')
                return render(request, 'appointment_booking.html', {'form': form})


            # Check if slot is already booked
            exists = Appointment.objects.filter(
                doctor=appointment.doctor,
                date=appointment.date,
                time_slot=appointment.time_slot
            ).exists()
            if not exists:
                # Handle payment method
                if appointment.payment_method == 'cash':
                    appointment.is_paid = False
                else:
                    appointment.is_paid = True  # Update after real payment gateway integration

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
    user = request.user
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
        return redirect('dashboard')  

    return render(request, 'book_lab_test.html')  # Use a dedicated template for lab test booking
        

@login_required
def reschedule_appointment(request, appointment_id):
    # Retrieve the existing appointment by ID (or 404 if it doesn't exist)
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    if request.method == 'POST':
        # Bind the form to the existing appointment instance
        form = RescheduleAppointmentForm(request.POST, instance=appointment)
        
        if form.is_valid():
            # Save the updated appointment details
            form.save()
            # After saving, you can redirect the user to a confirmation page or the updated appointment details
            return redirect('dashboard')
    else:
        # Initialize the form with the existing appointment data
        form = RescheduleAppointmentForm(instance=appointment)

    return render(request, 'reschedule_appointment.html', {'form': form, 'appointment': appointment})




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

@login_required
def cancel_lab_test(request, test_id):
    test = get_object_or_404(LabTestBooking, id=test_id, user=request.user)
    if request.method == 'POST':
        test.delete()
        messages.success(request, "Lab test booking cancelled successfully.")
        return redirect('dashboard')
    return redirect('dashboard')


