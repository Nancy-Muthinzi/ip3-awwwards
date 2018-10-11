from django.test import TestCase
from .models import Profile, Project

class ProfileTestClass(TestCase):
    def setUp(self):
        self.nancy = Profile(name = 'Nancy', email = 'kathinimuthinzi@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.nancy,Profile))    

    def test_save_method(self):
        self.nancy.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.nancy.save_profile()
        self.nancy.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)    