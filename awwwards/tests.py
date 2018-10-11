from django.test import TestCase
from .models import Profile, Project

class ProfileTestClass(TestCase):
    def setUp(self):
        self.nancy = Profile(name = 'Nancy', email = 'kathinimuthinzi@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.nancy,Profile))    
