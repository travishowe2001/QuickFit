from dataclasses import field
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from members.models import Account

class RegisterUserForm(UserCreationForm):
        
    email = forms.EmailField(max_length=60)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    weight = forms.IntegerField()
    username = forms.CharField(max_length=30)
    feet = forms.CharField(max_length=1)
    inches = forms.CharField(max_length=1)
    


    class Meta:
        model = Account
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'weight', 'feet', 'inches', 'password1', 'password2')
    