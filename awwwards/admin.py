from django.contrib import admin
from .models import Profile, Project, Rate

# class ProjectAdmin(admin.ModelAdmin):
    # filter_horizontal = ('rate',)
 
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Rate)
