from django.urls import path
from . import views

urlpatterns = [
    path('ESDdocli', views.ESDdocli, name='ESDdocli'),
    path('ansdoctorlist', views.ansdoclist, name='ansdoctorlist'),
    path('Cardiodoclist', views.cardoclist, name='Cardiodoclist'),
    path('ENTdocli', views.ENTdoclist, name='ENTdocli'),
    path('Gastrodocli', views.Gasdoclist, name='Gastrodocli'),
    path('Genedocli', views.Genedoclist, name='Genedocli'),
    path('Gynaecologydocli', views.Gynaecologydocli, name='Gynaecologydocli'),
    path('Hematologydocli', views.Hematologydocli, name='Hematologydocli'),
    
]