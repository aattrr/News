from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    tel = forms.CharField(max_length=12, required=False, help_text='Телефон')
    town = forms.CharField(max_length=36, required=False, help_text='Город')

    class Meta:
        model = User
        fields = ('username', 'tel', 'town', 'password1', 'password2')
