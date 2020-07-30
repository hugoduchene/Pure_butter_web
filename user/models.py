from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    pass

class UserSubscribeEmail(models.Model):
    id_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, unique=True)
    is_subscribe = models.BooleanField(default=True)
