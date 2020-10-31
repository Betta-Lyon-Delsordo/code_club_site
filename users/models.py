from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
LANGUAGE_CHOICES = [
    ('ENGLISH', 'English'),
    ('SPANISH', 'Spanish'),
]

ROLE_CHOICES = [
    ('MENTOR', 'Mentor'),
    ('STUDENT', 'Student'),
]


class CustomUser(AbstractUser):
    language = models.CharField(max_length=7, choices=LANGUAGE_CHOICES, default='ENGLISH',)
    role = models.CharField(max_length=7, choices=ROLE_CHOICES, default='MENTOR',)
    