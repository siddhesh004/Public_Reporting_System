from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from user.models import Public, User


class CivicSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_civic = True
        if commit:
            user.save()
        return user


class PublicSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self):
        user = super().save(commit=False)
        user.is_public = True
        user.save()
        return user

