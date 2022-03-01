from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Appointment(models.Model):
    at_name = models.CharField(max_length=100) #at=appointmenttake
    at_email = models.EmailField(max_length=254)
    a_taking_time = models.DateField(auto_now=False, auto_now_add=True) 
    doc_name = models.CharField(max_length=100)
    doc_email = models.EmailField(max_length=254)
    doc_department = models.CharField(max_length=150)
    a_taken_date = models.DateField(auto_now=False, auto_now_add=False)
    s_time = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.at_name}'s appointment"




