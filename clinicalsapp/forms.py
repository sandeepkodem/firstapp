from socket import fromshare
from django import forms
from .models import Patient,Clinicaldata
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PatienForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields="__all__"


class ClinicaldataForm(forms.ModelForm):
    class Meta:
        model=Clinicaldata
        fields="__all__"

class RegisterForm(UserCreationForm):

    class Meta:
        model=User
        fields=['username','email','password1','password2']