from django import forms
from .models import *
from django.contrib.auth.models import auth, User

class UserForm(forms.ModelForm):
	
	class Meta:
		model = User
		fields = ('email',)