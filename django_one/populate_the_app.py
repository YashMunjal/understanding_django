import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_one.settings')


import django
django.setup()

# Fake population scrypt
import random
from the_app.models import AccessRecord,Topic,Webpage
from faker import Faker