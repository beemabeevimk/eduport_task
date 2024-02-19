from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)



urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('authenticated_user', UserView.as_view(), name="currently_authenticated_user"),
    path('register', RegisterView.as_view(), name="register"),
    path('driver_register', DriverRegisterAPIView.as_view(), name="driver_register"),
    path('rider_register', RiderRegisterAPIView.as_view(), name="rider_register"),
    path('driver_profile_view', DriverProfileAPIView.as_view(), name="driver_profile"),
    path('registered_users',RegisteredUserView.as_view(), name = "registered_users"),
    path('logout', LogoutView.as_view(), name = "logout"),
]
