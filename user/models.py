from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_public = models.BooleanField(default=False)
    is_civic = models.BooleanField(default=False)


class Public(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        app_label = 'user'
