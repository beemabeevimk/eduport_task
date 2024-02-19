from django.contrib import admin
from .models import Account, Driver, Rider

# Register your models here.
admin.site.register(Account)
admin.site.register(Driver)
admin.site.register(Rider)