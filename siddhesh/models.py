from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.gis.db import models as gis_models




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


class Incidence(models.Model):
    desc = models.CharField(max_length=500)
    pos = gis_models.PointField(srid=4326)

    def __str__(self):
        return self.desc



