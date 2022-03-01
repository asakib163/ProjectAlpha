from bloodsection.models import Blood_donor, blood_bag_booking
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
def blooddonor(request):
    return render(request, 'blooddonors.html')

bginfo = blood_bag_booking.objects.all()
def bloodbank(request):
    bgbook = blood_bag_booking()
    if request.method == 'POST':
        bgbook.blood_requester_name = request.POST['fname']
        bgbook.email = request.POST['email']
        bgbook.blood_group = request.POST['bloodgroup']
        bgbook.contact = request.POST['contact']
        bgbook.booking_for_date = request.POST['booking_for']
        bgbook.bag_quantity = request.POST['quantity']
        bgbook.save()
        context={
            'name' : bgbook.blood_requester_name,
            'group' : bgbook.blood_group,
            'quantity' : bgbook.bag_quantity,
        }
        template = render_to_string('emailveri.html', context)
        email = EmailMessage(
            "Alpha Hospital room booking",
            template,
            settings.EMAIL_HOST_USER,
            [bgbook.email],
        )
        email.fail_silently = False
        email.send()
        return redirect('bgsuccess')

    return render(request, 'bloodbank.html')

def bgsuccess(request):
    return render(request, 'bgsuccess.html')

blddonor = Blood_donor.objects.all()
def bdregister(request):
    blooddonor = Blood_donor()
    link = 'bdregister'
    if request.method=='POST':
        blooddonor.fname = request.POST['name']
        blooddonor.uname = request.POST['username']
        blooddonor.email = request.POST['email']
        blooddonor.contact = request.POST['contact']
        blooddonor.profession = request.POST['profession']
        blooddonor.Blood_group = request.POST['bloodgroup']
        blooddonor.imag = request.POST['image']
        messages.info(request, 'you have successfully registerd')
        blooddonor.save()
        return redirect('bdregister')
        

    return render(request, 'bdregister.html', {'link':link})

def aplist(request):
    link = 'a+list'
    context = {
        'link':link,
        'bds' :blddonor,
    }
    return render(request, 'A+.html', context)

def bplist(request):
    link = 'b+list'
    context = {
        'link':link,
        'bds' :blddonor,
    }
    return render(request, 'B+.html',context)

def oplist(request):
    link = 'o+list'
    context = {
        'link':link,
        'bds' :blddonor,
    }
    return render(request, 'O+.html', context)

def abplist(request):
    link = 'ab+list'
    context = {
        'link':link,
        'bds' :blddonor,
    }
    return render(request, 'AB+.html', context)

def anlist(request):
    link = 'a-list'
    context = {
        'link':link,
        'bds' :blddonor,
    }
    return render(request, 'A-.html', context)

def bnlist(request):
    link = 'b-list'
    context = {
        'link':link,
        'bds' :blddonor,
    }
    return render(request, 'B-.html', context)

def onlist(request):
    link = 'o-list'
    context = {
        'link':link,
        'bds' :blddonor,
    }
    return render(request, 'O-.html', context)

def abnlist(request):
    link = 'ab-list'
    context = {
        'link':link,
        'bds' :blddonor,
    }
    return render(request, 'AB-.html', context)