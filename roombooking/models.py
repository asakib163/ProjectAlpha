from django.db import models

# Create your models here.
class roombook(models.Model):
    room_booker_name = models.CharField(max_length=50),
    room_booker_email = models.EmailField(max_length=254)
    room_booker_contact = models.CharField(max_length=20),
    room_category = models.CharField(max_length=50)
    room_booking_date = models.DateField(auto_now=False, auto_now_add=True)
    room_booking_for_date = models.DateField(auto_now=False, auto_now_add=False)