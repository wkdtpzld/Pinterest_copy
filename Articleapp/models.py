from django.db                      import models
from django.contrib.auth.models     import User

from projectapp.models import Projectapp

class Article(models.Model):
    writer      = models.ForeignKey(User, on_delete=models.SET_NULL , related_name='article', null=True)
    project     = models.ForeignKey(Projectapp, on_delete=models.SET_NULL,  related_name='article', null=True)
    title       = models.CharField(max_length=200, null=True)
    image       = models.ImageField(upload_to='article/', null=False)
    content     = models.TextField(null=True)
    create_at   = models.DateField(auto_now_add=True, null=True)