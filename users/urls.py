from django.urls import path
from django.utils.regex_helper import normalize
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('updateform', views.upform, name='updateform'),
    
]
