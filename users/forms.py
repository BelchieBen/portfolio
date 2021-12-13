from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class registrationForm(UserCreationForm):
	firstname = forms.CharField(max_length=120)
	surname = forms.CharField(max_length=120)
	email= forms.EmailField()

	class Meta:
		model = User
		fields = ['firstname','surname','email','password1','password2']
