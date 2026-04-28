from django.contrib import admin
from .models import FoodDonation, Request

admin.site.register(FoodDonation)
admin.site.register(Request)
from django.contrib.auth.models import User

try:
    user = User.objects.get(username="admin")
    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    user.save()
except:
    pass