from django.db import models
from django.contrib.auth.models import User


class FireAlert(models.Model):
    img = models.CharField(max_length=180)
    isFire = models.BooleanField(default=False)
    timestamp = models.DateTimeField(
        auto_now_add=True, auto_now=False, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.task
