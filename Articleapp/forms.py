from django.forms import ModelForm
from .models import Article
from django import forms
from projectapp.models import Projectapp

class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'editable' ,'style':'height: auto; text-align : left'}))

    project = forms.ModelChoiceField(queryset=Projectapp.objects.all(), required=False)

    class Meta:
        model = Article
        fields = ['title', 'image','project','content']
