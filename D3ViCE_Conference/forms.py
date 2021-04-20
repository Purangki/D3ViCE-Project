from django import forms
from .models import *

class ConferenceForm(forms.ModelForm):
	
	class Meta:
		model = Conference
		fields = ('title',)