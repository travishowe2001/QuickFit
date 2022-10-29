from django.urls import path
from . import views


app_name = 'members'

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('register_user', views.register_user, name='register_user'),
    path('profile', views.profile, name='profile'),
    path('change_password', views.change_password, name='change_password'),
    path('success', views.success, name='success')

]