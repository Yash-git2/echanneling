from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):  
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)

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


