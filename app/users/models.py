from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    course = models.CharField(max_length=100)  

    def __str__(self):
        return self.username 
