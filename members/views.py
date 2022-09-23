import imp
import re
from turtle import update
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from members.forms import RegisterUserForm
from members.models import Account
from .forms import RegisterUserForm
from django.contrib.auth.models import User
from utils import update_user_fields

import myFitness


# Create your views here.
def login_user(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect('/myFitness/')
        else:
            return redirect('/members/login_user')
            
    else:
        return render(request,'members/login.html')

def register_user(request):
    if request.method =="POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            update_user_fields(request,form)
            messages.success(request, 'Registration sucessfull.')
            return redirect('/myFitness/')
    else:
        form = RegisterUserForm()
    return render(request, 'members/register_user.html', {'form':form,})

def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out"))
    return redirect('/myFitness/')

