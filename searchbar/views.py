from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from bloodsection.models import Blood_donor

from doctors.models import Doctors

# Create your views here.

def searcheditems(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        docs = Doctors.objects.filter(doc_name__icontains = searched)
        blooddonors = Blood_donor.objects.filter(fname__icontains = searched)
        context = {
            'searched':searched,
            'docs': docs,
            'bds': blooddonors
        }
        return render(request, 'searchitems.html',context)
    else:
        return render(request, 'searchitems.html')
