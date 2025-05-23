# Generated by Django 5.2 on 2025-05-05 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_doctor_consultation_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='appointment',
            name='payment_method',
            field=models.CharField(choices=[('online', 'Online Payment'), ('cash', 'Cash at Visit')], default='online', max_length=10),
        ),
    ]
