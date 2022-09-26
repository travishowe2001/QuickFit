
from http.client import HTTPResponse
import string
from django.template import loader
from django.shortcuts import render, redirect
from members.models import Account
from utils import get_height, bmi_calc

# Create your views here.
def home(request):
    return render(request,'quickFit/home.html')

def gallery(request):
    template_path = "quickFit/home.html"
    
    context = {
        "images" : [
            "fitness.png",
        ]
    }

    return render(request, template_path,context)

def user_health(request):
    if request.user.is_authenticated:
        height = get_height( int(request.user.height_in_inches))
        height_in_inches = int(request.user.height_in_inches)
        weight = int(request.user.weight)
        bmi = bmi_calc(height_in_inches,weight)
        context = {'height': height, 'weight': weight, 'bmi':bmi}
        return render(request, "myfitness/health.html", context)
    else:
        return redirect("/members/login_user")

def about(request):
    return render(request, "quickfit/about.html")
    
