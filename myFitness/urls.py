from django.urls import path
from . import views
import myFitness

app_name = 'myFitness'

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path("gallery", views.gallery, name="gallery"),
    path("user_health", views.user_health, name='user_health')

]