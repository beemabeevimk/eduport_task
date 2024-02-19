# rides/serializers.py
from rest_framework import serializers
from .models import Ride
from accounts.serializers import RiderSerializer

class RideCreateSerializer(serializers.ModelSerializer):
    rider = RiderSerializer(read_only= True)
    class Meta:
        model = Ride
        fields = ("driver", "rider", "pickup_location", "dropoff_location")
        
    def create(self, validated_data):
        print("user serializer", validated_data)
        driver = validated_data['driver']
        pickup_location = validated_data['pickup_location']
        dropoff_location = validated_data['dropoff_location']
        # driver_instance = Driver.objects.get(id=driver)
        rider = self.context["request"].user.rider

        ride = Ride.objects.create(
            rider=rider,
            driver=driver,
            pickup_location=pickup_location,
            dropoff_location=dropoff_location,
        )
        return ride
    

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = "__all__"
