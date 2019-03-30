from django import forms
from django.contrib.auth.forms import UserCreationForm

from siddhesh.models import User, Public, Civic


class CivicSignUpForm(UserCreationForm):
    name = forms.CharField(
        widget=forms.TextInput,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_civic = True
        user.save()
        civic = Civic.objects.create(user=user)
        civic.name = self.cleaned_data.get('name')
        civic.save()
        return user


class PublicSignUpForm(UserCreationForm):
    name = forms.CharField(
        widget=forms.TextInput,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_public = True
        user.save()
        public = Public.objects.create(user=user)
        public.name = self.cleaned_data.get('name')
        public.save()
        return user
