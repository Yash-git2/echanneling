from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)

    def __str__(self):
        return f"Dr. {self.name} - {self.specialty}"

class Availability(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.TimeField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.doctor.name} - {self.date} at {self.time_slot}"
