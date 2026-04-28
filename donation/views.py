from django.shortcuts import render, redirect
from .models import FoodDonation, Request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


def home(request):
    foods = FoodDonation.objects.all()

    if request.user.is_authenticated:
        user = request.user
        requests = Request.objects.filter(requester=user)
    else:
        requests = []

    return render(request, 'home.html', {
        'foods': foods,
        'requests': requests
    })


def request_food(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    food = FoodDonation.objects.get(id=id)

    user = request.user

    Request.objects.create(
        food=food,
        requester=user
    )

    return redirect('home')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid credentials")

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')