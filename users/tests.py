
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import CustomUser

class UsersTests(TestCase):
    
  def setUp(self):
    self.user = get_user_model().objects.create_user(
      username='testuser',
      email='test@email.com',
      password='secret'
      
    )
    
    

  def test_sign_up_view(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'home.html')
  
  def test_user(self):
    self.assertEqual(self.user.username, 'testuser')
    self.assertEqual(self.user.email, 'test@email.com')
    
    
    

