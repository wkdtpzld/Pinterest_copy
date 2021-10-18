from django.forms import ModelForm
from .models import Projectapp

class ProjectCreationForm(ModelForm):
    class Meta:
        model = Projectapp
        fields = ['title', 'image', 'description']
