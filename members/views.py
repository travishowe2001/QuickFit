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

import quickFit


# Create your views here.
def login_user(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect('/quickFit/')
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
            return redirect('/quickFit/')
    else:
        form = RegisterUserForm()
    return render(request, 'members/register_user.html', {'form':form,})

def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out"))
    return redirect('/quickFit/')

def profile(request):
    return render(request, "members/profile.html")


def change_password(request):
    if request.method == "POST":
        current_password = request.POST["current_password"]
        new_password = request.POST["new_password"]
        confirm = request.POST["confirm_password"]
        
        if confirm == new_password:
            user_id = request.user.id
            user = Account.objects.get(id=user_id)
            user.set_password(new_password)
            user.save()
            return redirect('/members/success')
        else:
            return redirect('/quickfit/')

    else:
        return render(request, "members/change_password.html")
        
def success(request):
    return render(request, 'members/success.html')