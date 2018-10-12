from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Profile(models.Model):
    first_name = models.CharField(max_length = 25, default = "Nancy")
    last_name = models.CharField(max_length = 25, default = "Muthinzi")
    email = models.EmailField()
    phone_number = models.CharField(max_length = 15 ,blank = True)

   
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ['first_name', 'last_name']    


class Project(models.Model):
    title = models.CharField(max_length = 25)
    post = models.TextField() 
    description = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    project_image = models.ImageField(upload_to = 'projects/', blank = True)
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
        awwwards = cls.objects.filter(title)
        return awwwards    

    def __str__(self):
        return self.title 

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()