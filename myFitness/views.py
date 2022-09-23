
from http.client import HTTPResponse
import string
from django.template import loader
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'myFitness/home.html')

def gallery(request):
    template_path = "myFitness/home.html"
    
    context = {
        "images" : [
            "fitness.png",
        ]
    }

    return render(request, template_path,context)

def bmi_calculator(request):
    User.get
    user = Account.objects.get(username = username)
    return render(request,'myFitness/bmi.html')