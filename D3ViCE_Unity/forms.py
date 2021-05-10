from django import forms
from django.contrib.auth.models import AbstractUser
from D3ViCE_Conference.models import Conference
from D3ViCE_User.models import Profile,Participant

class UserLogin(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('username','password')

class UserUpdateAvatar(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('username','avatar_index')

class UserJoinConference(forms.ModelForm):

    class Meta:
        model = Conference
        fields = ('code',)

class RegisterParticipant(forms.ModelForm):

    class Meta:
        model = Participant
        fields = ('username',)