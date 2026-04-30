from django.shortcuts import render, redirect
from .models import FoodDonation, Request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


def home(request):
    # 🔹 ADD FOOD (donor)
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('login')

        name = request.POST.get("name")
        quantity = request.POST.get("quantity")
        location = request.POST.get("location")

        FoodDonation.objects.create(
            donor=request.user,
            food_name=name,
            quantity=quantity,
            location=location
        )

        return redirect('home')

    # 🔹 SHOW FOOD LIST
    foods = FoodDonation.objects.all()

    # 🔹 SHOW USER REQUESTS
    if request.user.is_authenticated:
        requests = Request.objects.filter(requester=request.user)
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

    Request.objects.create(
        food=food,
        requester=request.user
    )

    return redirect('home')


def signup_view(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        login(request, user)
        return redirect('home')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user:
            login(request, user)
            return redirect('home')

        return HttpResponse("Invalid credentials")

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')