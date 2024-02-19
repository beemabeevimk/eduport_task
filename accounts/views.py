# third party modules
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# local modules
from accounts.models import Account
from .serializers import UserRegisterSerializer, UserSerializer, AccountSerializer ,\
    DriverRegisterSerializer, RiderRegisterSerializer, DriverProfileSerializer, DriverProfileUpdateSerializer



# Custom Token Obtain Pair Serializer to include custom claims like email, name, and is_superuser.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):

        print(user, "login side in server")
        token = super().get_token(user)

        # Add custom claims
        
        token['email'] = user.email
        token['name'] = user.name
        token['is_superuser'] = user.is_superuser
        
        return token

"""
Implement API endpoints for user registration and login 

"""

# Custom Token Obtain Pair View using the custom serializer.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
    
# View for user registration.   
class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserRegisterSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
# View for driver registration. 
class DriverRegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = DriverRegisterSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


# View for viewing driver profile and update profile. 
class DriverProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        driver = user.driver 
        serializer = DriverProfileSerializer(driver)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request):
        data = request.data
        user = request.user
        driver = user.driver 
        serializer = DriverProfileUpdateSerializer(driver,data=data)
        if serializer.is_valid():
            serializer.save() 
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  

class RiderRegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        # print(data)
        serializer = RiderRegisterSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  



# currently authenticated user
class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class RegisteredUserView(APIView):
    permission_classes = [permissions.IsAdminUser]
    print('got to user getting api function')
    def get(self,request):
        print('User making the request:', request.user) 
        user = Account.objects.exclude(is_superuser=True)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)  
    
    

class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
            return Response("Logout Successful", status=status.HTTP_200_OK)
        except TokenError:
            raise AuthenticationFailed("Invalid Token")
  
from rest_framework.decorators import action        
from rest_framework import viewsets     
class AccountsViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    
    @action(detail=False)
    def list_drivers(self, request):
        drivers = Account.objects.filter(user_type="DRIVER").order_by('-last_login')

        page = self.paginate_queryset(drivers)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(drivers, many=True)
        return Response(serializer.data)