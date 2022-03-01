from django.urls import path
from . import views

urlpatterns = [
    path('rooms', views.room, name='rooms'),
    path('booksuccess', views.booksuccess, name='booksuccess'),
]
