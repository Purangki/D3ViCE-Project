from django import forms
from django.contrib.auth.models import AbstractUser
from django.forms import fields
from D3ViCE_Conference.models import Conference, Question
from D3ViCE_User.models import Profile  # ,Participant
# from .models import *
# from django.contrib.auth import login, logout
# from django.contrib.auth.models import auth, User


class UserLogin(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('username', 'password')


class UserUpdateAvatar(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('username', 'avatar_index')


class UserJoinConference(forms.ModelForm):

    class Meta:
        model = Conference
        fields = ('code',)


class RegisterParticipant(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('username',)


class UpdateUserProfile(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('username',)


class AddQuestion(forms.Form):

    class Meta:
        model = Question
        fields = ('user',)


class GetQuestions(forms.Form):

    class Meta:
        model = Question
        fields = ('conference',)
