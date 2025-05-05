from django import forms
from .models import Appointment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Appointment, Doctor


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




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

    # ✅ Use RadioSelect for payment method
    payment_method = forms.ChoiceField(
        choices=Appointment.PAYMENT_METHOD_CHOICES,
        widget=forms.RadioSelect
    )

    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time_slot', 'payment_method']

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)

        # Only show actual doctors in the dropdown
        self.fields['doctor'].queryset = Doctor.objects.all()

        # Optional: Add placeholders and form styling
        self.fields['date'].widget.attrs.update({'placeholder': 'YYYY-MM-DD'})
        self.fields['time_slot'].widget.attrs.update({'placeholder': 'e.g. 10:00 AM'})
        self.fields['payment_method'].widget.attrs.update({'class': 'form-control'})

