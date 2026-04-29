import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "food_project.settings")
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser(
        username="admin",
        email="admin@gmail.com",
        password="admin123"
    )
    print("Admin created")
