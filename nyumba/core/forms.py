from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import  gettext_lazy as _

class RegisterForm(UserCreationForm):
    username=forms.CharField(max_length=20)
    email=forms.CharField(max_length=200)
    password1=forms.CharField(label=_("password"),widget=forms.PasswordInput())
    password2=forms.CharField(label=_("confirm password"),widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=["username","email","password1","password2"]

    
    
    

