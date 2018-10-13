from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile', default=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='profile/', default=True)
    bio = models.CharField(max_length=200, default=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
       
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @receiver(post_save, sender=User)
    def create_user_profile(self, sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)    

    @receiver(post_save, sender=User)
    def save_user_profile(self, sender, instance, **kwargs):
        instance.profile.save()
        

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ['first_name', 'last_name']    


class Project(models.Model):
    title = models.CharField(max_length = 25) 
    description = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    project_image = models.ImageField(upload_to = 'projects/')
    link = models.CharField(max_length=50, blank=True)
    pub_date = models.DateTimeField(auto_now_add = True)

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def search_by_title(cls, search_term): 
        awwwards = cls.objects.filter (title__icontains = search_term)
        return awwwards

    @classmethod
    def projects(cls):
        today = dt.date.today()
        awwwards = cls.objects.filter(title)
        return awwwards    

    def __str__(self):
        return self.title 


class Rate(models.Model):
    rate = models.CharField(max_length=144)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=True)
    user = models.ForeignKey(User, default=True, on_delete=models.CASCADE)

    def save_rate(self):
        self.save()

    def delete_rate(self):
        self.delete()

    def __str__(self):
        return self.rate


class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()