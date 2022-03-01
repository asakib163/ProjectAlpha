from doctors.models import Doctors
from django.shortcuts import render

# Create your views here.
docs = Doctors.objects.all()
def ESDdocli(request):
    link = 'ESDdocli'
    context = {
        'docs': docs,
        'link' : link
    }
      
    return render(request, 'ESDdocli.html', context)

def ansdoclist(request):
    link = 'ansdoctorlist'
    context = {
        'docs': docs,
        'link' : link
    } 
    return render(request, 'ansdoctorlist.html',context )

def cardoclist(request):
    link = 'Cardiodoclist'
    context = {
        'docs': docs,
        'link' : link
    }
    return render(request, 'Cardiodoclist.html' , context)

def ENTdoclist(request):
    link = 'ENTdocli'
    context = {
        'docs': docs,
        'link' : link
    }
    return render(request, 'ENTdocli.html' , context)

def Gasdoclist(request):
    link = 'Gastrodocli'
    context = {
        'docs': docs,
        'link' : link
    }
    return render(request, 'Gastrodocli.html' , context)

def Genedoclist(request):
    link = 'Genedocli'
    context = {
        'docs': docs,
        'link' : link
    }
    return render(request, 'Genedocli.html' , context)

def Gynaecologydocli(request):
    link = 'Gynaecologydocli'
    context = {
        'docs': docs,
        'link' : link
    }
    return render(request, 'Gynaecologydocli.html' , context)

def Hematologydocli(request):
    link = 'Hematologydocli'
    context = {
        'docs': docs,
        'link' : link
    }
    return render(request, 'Hematologydocli.html' , context)

