from django.urls import path
from .views import CreateRideView, ListRidesView, RideDetailView, RideStatusUpdateView, RideCurrentLocationUpdateView, RideAcceptView, AvailableDriversListAPIView


urlpatterns = [

    path('create_new_ride/', CreateRideView.as_view(), name='create_ride'),
    path('rides_list/', ListRidesView.as_view(), name='list_rides'),
    path('available_drivers_list/', AvailableDriversListAPIView.as_view(), name='available_drivers'),
    path('rides_detail/<int:ride_id>/', RideDetailView.as_view(), name='ride_detail'),
    path('rides_status/<int:ride_id>/status/', RideStatusUpdateView.as_view(), name='update_ride_status'),
    path('rides_location/<int:ride_id>/location/', RideCurrentLocationUpdateView.as_view(), name='ride-location-update'),
    path('rides/<int:ride_id>/accept/', RideAcceptView.as_view(), name='ride-accept'),
]
