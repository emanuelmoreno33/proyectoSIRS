from django import forms
from django.contrib.auth.forms import UserCreationForm

class loginForm(forms.Form):
	username = forms.CharField(max_length=24, widget=forms.TextInput())
	password = forms.CharField(max_length=24, widget=forms.PasswordInput())


class Users_form(UserCreationForm):
	email = forms.CharField(max_length=48)
