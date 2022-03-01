from django.urls import path
from . import views

urlpatterns = [
    path('ambdetails', views.ambdetails, name='ambdetails'),
]