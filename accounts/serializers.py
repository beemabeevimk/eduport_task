from rest_framework import serializers
from accounts.models import Account, Rider, Driver
from rest_framework.validators import ValidationError


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id','name', 'email', 'user_type')


# user register serializer
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id','name', 'email', 'password', 'user_type')
        
    def create(self, validated_data):
        print("user serializer", validated_data)
        name = validated_data['name']
        email = validated_data['email']
        password = validated_data['password']
        user_type = validated_data['user_type']

        user = Account.objects.create_user(
            name=name,
            email=email,
            password=password,
            user_type=user_type,
        )
        return user



class DriverRegisterSerializer(serializers.ModelSerializer):
    vehicle_type = serializers.IntegerField(required=True,write_only=True)
    address = serializers.CharField(required=True,write_only=True)
    age = serializers.IntegerField(required=True,write_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Account
        fields = ('id','name', 'email', 'password',"vehicle_type","address","age",)
        
    def validate(self, attrs):
        vehicle_type=attrs['vehicle_type']
        if vehicle_type not in [1,2]:
            raise ValidationError(f"vehicle_type {vehicle_type} not a valid choice")
        return attrs
    
    def create(self, validated_data):
        print("user serializer", validated_data)
        name = validated_data['name']
        email = validated_data['email']
        password = validated_data['password']
        vehicle_type = validated_data['vehicle_type']
        address = validated_data['address']
        age = validated_data['age']

        user = Account.objects.create_user(
            name=name,
            email=email,
            password=password,
            user_type="DRIVER",
        )
        Driver.objects.create(
            user=user,
            vehicle_type=vehicle_type,
            address=address,
            age=age
        )
        return user


class RiderRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Account
        fields = ('id','name', 'email', 'password',)
        
    def create(self, validated_data):
        print("user serializer", validated_data)
        name = validated_data['name']
        email = validated_data['email']
        password = validated_data['password']

        user = Account.objects.create_user(
            name=name,
            email=email,
            password=password,
            user_type="RIDER",
        )
        Rider.objects.create(
            user=user,
        )
        return user


# user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ( 'id','name', 'email', 'password','address')
        
        
class DriverProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="user.name")
    email = serializers.CharField(source="user.email",read_only=True)
    class Meta:
        model = Driver
        exclude = ('created_at', 'updated_at', 'is_deleted')
        
    
class DriverProfileUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    email = serializers.CharField(read_only=True,source="user.email")
    class Meta:
        model = Driver
        fields = ('name','address','age','email','vehicle_type')
    
    
class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = "__all__"
        

class DriverSerializer(serializers.ModelSerializer):
    driver_name = serializers.CharField(source="user.name",read_only=True)
    email = serializers.CharField(source="user.email",read_only=True)
    class Meta:
        model = Driver
        fields = "__all__"
