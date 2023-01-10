from django.db import models
from django.contrib.auth.models import User

class Messages(models.Model):
    messages = models.TextField(default="Just to Say Hi")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, default="Unknown")

# Create your models here.