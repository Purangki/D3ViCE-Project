from django import forms
from django.contrib.auth.models import AbstractUser
from D3ViCE_Conference.models import Conference

class UserJoin(forms.ModelForm):

    class Meta:
        model = Conference
        fields = ('code',)

class RegisterParticipants(forms.ModelForm):

    class Meta:
        model = AbstractUser
        field = ('username',)