from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length = 25, default = "Nancy Muthinzi")
    email = models.EmailField()
   
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()