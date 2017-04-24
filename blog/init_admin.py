import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
django.setup()
from django.contrib.auth.models import User
try:
    admin = User.objects.get(username='tom')
except:
    User.objects.create_superuser('tom', 'tom@example.com', '123')
