from django.contrib import admin
from .models import FoodDonation, Request


@admin.register(FoodDonation)
class FoodDonationAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'quantity', 'location', 'status', 'donor')
    list_filter = ('status',)
    search_fields = ('food_name', 'location')


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('food', 'requester', 'status')
    list_filter = ('status',)