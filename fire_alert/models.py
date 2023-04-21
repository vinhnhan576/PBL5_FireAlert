from django.db import models
from django.contrib.auth.models import User
from datetime import date

class FireAlert(models.Model):
    img = models.CharField(max_length=180)
    isFire = models.BooleanField(default=False)
    timestamp = models.DateTimeField(
        auto_now_add=True, auto_now=False, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.task

class FireAlertExpoToken(models.Model):
    expo_token = models.CharField(max_length=300)
    
    def __str__(self):
        return self.task

class Image(models.Model):
    image = models.ImageField(upload_to='images')
    timestamp = models.TimeField((""), auto_now=True, auto_now_add=False)