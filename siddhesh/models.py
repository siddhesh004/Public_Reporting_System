from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_public = models.BooleanField('public', default=False)
    is_civic = models.BooleanField('civic', default=False)


class Public(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Civic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
