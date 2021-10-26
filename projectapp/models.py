from django.db import models


class Projectapp(models.Model):
    title       = models.CharField(max_length=20, null=False)
    image       = models.ImageField(upload_to='project/', null=False)
    created_at  = models.DateTimeField(auto_now_add=True,null=True)
    description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.title}'