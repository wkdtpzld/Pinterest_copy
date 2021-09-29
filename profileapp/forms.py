from django.forms import ModelForm
from . import models

class Profile_Creation_Form(ModelForm):
    class Meta:
        model = models.Profile
        fields = ['image','nickname','message']