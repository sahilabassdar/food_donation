from django.contrib import admin
from .models import FoodDonation, Request

admin.site.register(FoodDonation)
admin.site.register(Request)