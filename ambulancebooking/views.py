from django.shortcuts import render

# Create your views here.

def ambdetails(request):
    return render(request, 'ambulancedetails.html')
