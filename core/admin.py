from django.contrib import admin
from .models import Appointment
from .models import Doctor
from .models import DoctorAvailability

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'consultation_fee')  # Add your custom fields here


admin.site.register(Doctor)
admin.site.register(DoctorAvailability)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'doctor', 'date', 'time_slot', 'payment_method', 'is_paid')

admin.site.register(Appointment, AppointmentAdmin)