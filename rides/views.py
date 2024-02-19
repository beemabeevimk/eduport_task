# third party modules
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
# local modules
from .models import Ride
from .serializers import RideSerializer, RideCreateSerializer
from accounts.models import Driver
from accounts.serializers import DriverSerializer

"""
API endpoint for creating a ride request
"""
class CreateRideView(APIView):
    def post(self, request):
        rider_user = request.user.rider
        serializer = RideCreateSerializer(data=request.data, context= {'request':request})
        if serializer.is_valid():
            # serializer.rider = rider_user      
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
"""
API endpoint for listing all rides.
"""
class ListRidesView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        if request.user.user_type == "DRIVER":
            rides = Ride.objects.filter(driver = request.user.driver)
        else:
            rides = Ride.objects.filter(rider = request.user.rider)
        serializer = RideSerializer(rides, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

"""
API endpoint for Listing available drivers
"""
class AvailableDriversListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        rides = list(Ride.objects.filter(status__in=["STARTED","ACCEPTED"]).values_list('driver',flat=True))
        active_drivers_id = list(set(rides)) 
        drivers = Driver.objects.select_related("user").all().exclude(id__in= active_drivers_id) 
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

"""
API endpoint for viewing a ride's details
"""
class RideDetailView(APIView):
    def get(self, request, ride_id):
        ride = Ride.objects.filter(id=ride_id).first()
        if ride:
            serializer = RideSerializer(ride)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'Ride not found'}, status=status.HTTP_404_NOT_FOUND)


"""
API endpoint for updating the status of a ride
"""
class RideStatusUpdateView(APIView):
    def patch(self, request, ride_id):
        try:
            ride = Ride.objects.get(id=ride_id)
            new_status = request.data.get('status')
            if new_status in dict(Ride.STATUS_CHOICES):
                ride.status = new_status
                ride.save()
                return Response({'message': 'Ride status updated successfully'})
            return Response({'message': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)
        except Ride.DoesNotExist:
            return Response({'message': 'Ride not found'}, status=status.HTTP_404_NOT_FOUND)
        
        
        
"""
API endpoint for real-time ride tracking
"""
class RideCurrentLocationUpdateView(APIView):
    def patch(self, request, ride_id):
        try:
            ride = Ride.objects.get(id=ride_id)
            current_location = request.data.get('current_location')
            ride.current_location = current_location
            ride.save()
            return Response({'message': 'Ride current location updated successfully'})
        except Ride.DoesNotExist:
            return Response({'message': 'Ride not found'}, status=status.HTTP_404_NOT_FOUND)
        
        

class RideAcceptView(APIView):
    """
    API endpoint for drivers to accept a ride request,
    
    """
    def get(self, request, ride_id):
        try:
            driver=Driver.objects.filter(user=request.user).first()
            print(driver)
            ride = Ride.objects.get(id=ride_id)
            print(ride.driver)
            if driver:
               if ride.driver!=driver:
                    return Response({'message': 'Access denied'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Access denied'}, status=status.HTTP_400_BAD_REQUEST)
            if ride.status == 'REQUESTED':
                ride.status = 'ACCEPTED'
                ride.save()
                return Response({'message': 'Ride request accepted successfully'})
            else:
                return Response({'message': 'Ride request is not requested'}, status=status.HTTP_400_BAD_REQUEST)
        except Ride.DoesNotExist:
            return Response({'message': 'Ride request not found'}, status=status.HTTP_404_NOT_FOUND)
        
    