# local modules
from django.db import models
from accounts.models import Rider, Driver

"""
Django model for Rides
"""

class Ride(models.Model):
    STATUS_CHOICES = [
        ('REQUESTED', 'Requested'),
        ('ACCEPTED', 'Accepted'),
        ('STARTED', 'Started'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    rider = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name='rides_as_rider')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='rides_as_driver', null=True, blank=True)
    pickup_location = models.JSONField(default=dict)
    dropoff_location = models.JSONField(default=dict)
    current_location = models.JSONField(default=dict)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='REQUESTED')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Ride {self.id} - {self.rider.user.email}'