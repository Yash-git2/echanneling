#Add forms.py for handling user input forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


from .models import Appointment, Doctor

class AppointmentForm(forms.ModelForm):
    # ✅ Dummy time slots for now
    TIME_CHOICES = [
        ("09:00 AM", "09:00 AM"),
        ("10:00 AM", "10:00 AM"),
        ("11:00 AM", "11:00 AM"),
        ("12:00 PM", "12:00 PM"),
        ("01:00 PM", "01:00 PM"),
        ("02:00 PM", "02:00 PM"),
        ("03:00 PM", "03:00 PM"),
        ("04:00 PM", "04:00 PM"),
    ]

    # ✅ Override time_slot field from model
    time_slot = forms.ChoiceField(choices=TIME_CHOICES)

    # ✅ Doctor dropdown from model
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all())

    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time_slot']
