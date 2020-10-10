from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
LANGUAGE_CHOICES = [
    ('ENGLISH', 'English'),
    ('SPANISH', 'Spanish'),
]



class CustomUser(AbstractUser):
    language = models.CharField(max_length=7, choices=LANGUAGE_CHOICES)
    