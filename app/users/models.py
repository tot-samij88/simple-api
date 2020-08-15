from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    messages = models.CharField(max_length=1000, unique=True)
    owner = models.ForeignKey(
        User, related_name='users', on_delete=models.CASCADE, null=True)
    
