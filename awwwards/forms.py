from .models import Project

class NewProjectForm(forms:Model.Form):
    class Meta:
        model = Project
        exclude = ['profile', 'pub_date']