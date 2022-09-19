from django.urls import path
from . import views
import myFitness

app_name = 'myFitness'

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path("gallery", views.gallery, name="gallery"),
    path('bmi_calculator', views.bmi_calculator, name='bmi_calculator')

]