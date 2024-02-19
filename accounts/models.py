
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .utils import VehicleTypes

 # custom manager
class AccountManager(BaseUserManager): 
    def create_user(self, name, email, user_type, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            name=name,
            email=email,
        )
        user.set_password(password)
        user.user_type = user_type
        user.save(using=self._db)
        return user

    def create_superuser(self, name,email, password=None):
        user = self.create_user(name, email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    

class Account(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = [
        ('DRIVER', 'Driver'),
        ('RIDER', 'Rider'),
    ]
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=300, null=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES,default="RIDER")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = AccountManager()

    def __str__(self):
        return self.name
    
    
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        abstract = True

      
class Driver(BaseModel):
    VEHICLE_CHOICES = [
        (VehicleTypes.TWO_WHEELER , 'Two wheeler'),
        (VehicleTypes.FOUR_WHEELER, 'Four wheeler'), 
    ]
    DRIVER_STATUS_CHOICES = [
        ('REQUESTED', 'Requested'),
        ('PROCESSING', 'Processing'),
        ('VERIFIED', 'Verified'),
    ]
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="driver")
    avatar = models.ImageField(upload_to="profiles/driver",null=True,blank=True)
    vehicle_type = models.PositiveIntegerField(choices=VEHICLE_CHOICES,default=VehicleTypes.TWO_WHEELER)
    address = models.TextField(null=True)
    age = models.IntegerField(default=0)
    status = models.CharField(max_length=25, choices=DRIVER_STATUS_CHOICES)
    def __str__(self) -> str:
        return self.user.email
    

class Rider(BaseModel):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="rider") 
    avatar = models.ImageField(upload_to="profiles/rider",null=True,blank=True)
    def __str__(self) -> str:
        return self.user.name
        
        




    

