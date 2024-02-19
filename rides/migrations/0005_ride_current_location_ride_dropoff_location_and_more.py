# Generated by Django 5.0.1 on 2024-02-18 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0004_remove_ride_dropoff_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='current_location',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='ride',
            name='dropoff_location',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='ride',
            name='pickup_location',
            field=models.JSONField(default=dict),
        ),
    ]
