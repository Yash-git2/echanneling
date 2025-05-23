# Generated by Django 3.2.25 on 2025-05-04 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabTestBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('test', models.CharField(max_length=50)),
                ('preferred_date', models.DateField(blank=True, null=True)),
                ('preferred_time', models.TimeField()),
                ('prescription', models.FileField(blank=True, null=True, upload_to='prescriptions/')),
                ('notes', models.TextField(blank=True)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
