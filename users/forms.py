from django.contrib.auth import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField(label="First Name")
	last_name = forms.CharField(label="last Name")

	class Meta:
		model = User
		fields = ['username', 'email','first_name', 'last_name', 'password1', 'password2']

class ProfileAddressForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['address', 'phone_number']




