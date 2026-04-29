import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "food_project.settings")
django.setup()

from django.contrib.auth.models import User

username = "admin"
password = "admin123"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(
        username=username,
        email="admin@gmail.com",
        password=password
    )
    print("Render admin created")
else:
    print("Admin already exists")
