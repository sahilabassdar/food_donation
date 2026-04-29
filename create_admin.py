import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_project.settings')
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username="admin3").exists():
    User.objects.create_superuser(
        username="admin3",
        email="admin@gmail.com",
        password="admin123"
    )
    print("Admin created")
else:
    print("Admin already exists")