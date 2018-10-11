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

class ProjectTestClass(TestCase):
    def setUp(self):
        self.nancy = Profile(name = 'Nancy', email = 'kathinimuthinzi@gmail.com')
        self.nancy.save_profile()

    def setUp(self):
        self.new_project = Project(title = 'Test Project', post = 'This is a random test post', profile = self.nancy)
        self.new_project.save()  

    def tearDown(self):
        Profile.objects.all().delete()
        Project.objects.all().delete()    

    def test_save_method(self):
        self.test_project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)  

    def test_delete_method(self):
        self.test_project.save_project()
        self.nancy.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 0) 

    def test_get_projects(self):
        projects = Project.projects()
        self.assertTrue(len(projects)>0)
