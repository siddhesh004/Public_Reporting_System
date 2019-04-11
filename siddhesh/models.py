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
    pos = gis_models.PointField(srid=4326, blank=True, null=True)
    locality = models.CharField(max_length=100,default='')
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.desc


class Vote(models.Model):

    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    incidence = models.ForeignKey(Incidence, related_name='incidence', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'incidence')




