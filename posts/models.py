from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.
COVER_CHOICES = [
    ('default.jpg', 'Default'),
    ('ep3.jpg', 'ep3'),
    ('ep4.jpg', 'ep4'),
    ('ep5.jpg', 'ep5'),
    ('ep8.jpg', 'ep8'),
    ('intro.jpg', 'intro'),
    ('intro2.jpg', 'intro2'),
]



class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    cover = models.ImageField(choices=COVER_CHOICES, default='default.jpg')
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])