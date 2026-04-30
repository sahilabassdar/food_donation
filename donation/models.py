from django.db import models
from django.contrib.auth.models import User


# ✅ Food status choices
STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
]


class FoodDonation(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.food_name


# ✅ Request status choices
REQUEST_STATUS = [
    ('Requested', 'Requested'),
    ('Accepted', 'Accepted'),
    ('Rejected', 'Rejected'),
]


class Request(models.Model):
    food = models.ForeignKey(FoodDonation, on_delete=models.CASCADE)
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=REQUEST_STATUS, default='Requested')

    def __str__(self):
        return f"{self.food.food_name} requested by {self.requester.username}"