from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import CustomUser

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'password')
