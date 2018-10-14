from django import forms
from .models import Project

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='Names',max_length=30)
    email = forms.EmailField(label='Email')
    
class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile', 'pub_date']
        widgets = {
            'like': forms.CheckboxSelectMultiple(),
        }    