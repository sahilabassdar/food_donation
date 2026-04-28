"""
URL configuration for food_project project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path
from donation import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('request/<int:id>/', views.request_food, name='request_food'),

    # Authentication
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]