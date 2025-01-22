from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser) :
    profile_img =models.ImageField(default='default.png',upload_to='images/')
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField()
    address = models.CharField(max_length=50)

