from turtle import update
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from members.forms import RegisterUserForm
from members.models import Account
from django.contrib.auth.models import User

#This function is used in the "register_user" view to update the users fields using the user creation form
def update_user_fields(request,form):
    username = form.cleaned_data['username']
    password = form.cleaned_data['password1']
    feet = form.cleaned_data['feet']
    inches = form.cleaned_data['inches']
    u = Account.objects.get(username = username)
    u.height_in_inches = (int(feet) * 12) + int(inches)
    u.height = feet + "'" + inches
    u.save(update_fields=['height','height_in_inches'])
    user = authenticate(username=username, password=password)
    login(request, user)