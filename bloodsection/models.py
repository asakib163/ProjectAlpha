from django.db import models
from django.db.models.fields.files import ImageField
from PIL import Image

# Create your models here.
class Blood_donor(models.Model):
    fname = models.CharField(max_length=50)
    uname = models.CharField(max_length=50)
    imag = models.ImageField(default = 'default1.jpg', upload_to='blood_donors_pics', null=True)
    Blood_group = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    contact = models.CharField(max_length=50)
    profession = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.fname}'
    
    def save(self):
        super().save()
        img = Image.open(self.imag.path)
        if img.height >500 or img.width>500:
            output_size = (500,500)
            img.thumbnail(output_size)
            img.save(self.imag.path)

class blood_bag_booking(models.Model):
    blood_requester_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    blood_group = models.CharField(max_length=50)
    bag_quantity = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    booking_date = models.DateField(auto_now=False, auto_now_add=True)
    booking_for_date = models.DateField(auto_now=False, auto_now_add=False)