from django.shortcuts import redirect, render
from .models import roombook
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
def room(request):
    room = roombook()
    if request.method == 'POST':
        room.room_booker_name = request.POST['fname']
        room.room_booker_email = request.POST['email']
        room.room_booker_contact = request.POST['contact']
        room.room_booking_for_date = request.POST['booking_for']
        room.room_category = request.POST['room_category']
        room.save()
         
        impdata = {
            'rbn' : room.room_booker_name,
            'rbfd': room.room_booking_for_date,
            'rc'  : room.room_category,
        }
        template = render_to_string('emailverifi.html', impdata)
        email = EmailMessage(
            "Alpha Hospital room booking",
            template,
            settings.EMAIL_HOST_USER,
            [room.room_booker_email],
        )
        email.fail_silently = False
        email.send()
        return redirect('booksuccess')
        
    return render(request, 'roombook.html')

def booksuccess(request):
    return render(request, 'booksuccess.html')

