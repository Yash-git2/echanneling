from django.contrib import admin
from .models import Doctor, Availability

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'hospital')

@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'date', 'time_slot', 'is_available')
    list_filter = ('doctor', 'date', 'is_available')
