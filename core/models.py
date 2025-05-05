from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    qualification = models.TextField(blank=True, null=True)
    availability = models.BooleanField(default=True)
    image = models.ImageField(upload_to='doctor_images/', null=True, blank=True)
    rating = models.FloatField(default=0.0)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.name} - {self.specialty}"

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.CharField(max_length=50)

    class Meta:
        unique_together = ('doctor', 'date', 'time_slot')  # Prevent double bookings

    def __str__(self):
        return f"{self.user.username} - {self.doctor.name} - {self.date} {self.time_slot}"



class DoctorAvailability(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.doctor.username} - {self.date} ({self.start_time} to {self.end_time})"
    


class LabTestBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    time_slot = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username} - {self.test_name} on {self.date}"