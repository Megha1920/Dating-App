from django.db import models
import uuid
from datetime import datetime

class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    mobile = models.CharField(max_length=55, default="0123")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
