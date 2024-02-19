# Generated by Django 5.0.1 on 2024-02-18 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0003_alter_ride_driver_alter_ride_rider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='dropoff_location',
        ),
        migrations.RemoveField(
            model_name='ride',
            name='pickup_location',
        ),
        migrations.AlterField(
            model_name='ride',
            name='status',
            field=models.CharField(choices=[('REQUESTED', 'Requested'), ('ACCEPTED', 'Accepted'), ('STARTED', 'Started'), ('COMPLETED', 'Completed'), ('CANCELLED', 'Cancelled')], default='REQUESTED', max_length=20),
        ),
    ]
