from .models import Comment
from django.forms import ModelForm

class Comment_Creation_Form(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']