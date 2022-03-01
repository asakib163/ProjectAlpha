from django.urls import path
from . import views

urlpatterns = [
    path('blooddonors', views.bdregister, name='blooddonors'),
    path('bloodbank', views.bloodbank, name='bloodbank'),
    path('bdregister', views.bdregister, name='bdregister'),
    path('bgsuccess', views.bgsuccess, name='bgsuccess'),
    path('a+list', views.aplist, name='a+list'),
    path('b+list', views.bplist, name='b+list'),
    path('o+list', views.oplist, name='o+list'),
    path('ab+list', views.abplist, name='ab+list'),
    path('a-list', views.anlist, name='a-list'),
    path('b-list', views.bnlist, name='b-list'),
    path('o-list', views.onlist, name='o-list'),
    path('ab-list', views.abnlist, name='ab-list'),
]
