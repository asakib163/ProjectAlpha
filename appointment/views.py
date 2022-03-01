from appointment.models import Appointment
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage

from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.

@login_required
def appointment(request):
    
    doc_name = request.POST.get('doc_name', None)
    doc_image = request.POST.get('img', None)
    doc_speciality = request.POST.get('doc_speciality', None)
    doc_email = request.POST.get('doc_email', None)
    doc_department = request.POST.get('doc_department', None)
    doc_degree = request.POST.get('doc_degree', None)
    doc_experiance = request.POST.get('doc_experiance', None)
    doc_contact = request.POST.get('doc_contact', None)



    context = {
        'doc_name'  : doc_name,
        'doc_img'   : doc_image,
        'doc_speciality':doc_speciality,
        'doc_email' : doc_email,
        'doc_department' : doc_department,
        'doc_degree'    : doc_degree,
        'doc_experiance'    : doc_experiance,
        'doc_contact'   : doc_contact,
        
    }
    return render(request, 'appointment.html', context)


@login_required
def appsuccess(request):
    app = Appointment()
    if request.method == 'POST':
        
        app.at_name = request.POST['user_name']
        app.at_email = request.POST['user_email']
        app.doc_name = request.POST['doc_name']
        app.doc_email = request.POST['doc_email']
        app.doc_department = request.POST['doc_department']
        app.s_time = request.POST['shedule']
        app.a_taken_date = request.POST['date']

        app.save()
    


    impdata = {
        'user' : app.at_name,
        'doc_name' : app.doc_name,
        'doc_dept': app.doc_department,
        'date' : app.a_taken_date,
        'time' : app.s_time,
    }

    template = render_to_string('emailverification.html', impdata)
    email = EmailMessage(
        "Alpha Hospital Doctor's appointment",
        template,
        settings.EMAIL_HOST_USER,
        [app.at_email],
    )
    email.fail_silently = False
    email.send()
    return render(request, 'appsuccess.html')
