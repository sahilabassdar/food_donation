from django.contrib import admin
from django.urls import path
from donation import views

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # Custom Admin Dashboard
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Main Page
    path('', views.home, name='home'),

    # Food Request
    path('request/<int:id>/', views.request_food, name='request_food'),

    # Authentication
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]