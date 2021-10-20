from django.db                  import models
from django.contrib.auth.models import User

from projectapp.models import Projectapp


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscription")
    project = models.ForeignKey(Projectapp, on_delete=models.CASCADE, related_name="subscription")

    class Meta:
        unique_together = ('user','project')