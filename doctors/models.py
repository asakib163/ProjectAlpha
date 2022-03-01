from django.db import models
from PIL import Image

# Create your models here.
class Doctors(models.Model):
    doc_name = models.CharField(max_length=50)
    img = models.ImageField(default = 'default1.jpg', upload_to='doctor_pics')
    email = models.EmailField(max_length=50)
    contact_no = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    Speciality = models.CharField(max_length=50)
    degree = models.CharField(max_length=200)
    experiance = models.CharField(max_length=200)

    def __str__(self):
        return f'Doctor {self.doc_name}'
    
    def save(self):
        super().save()
        img = Image.open(self.img.path)
        if img.height >500 or img.width>500:
            output_size = (500,500)
            img.thumbnail(output_size)
            img.save(self.img.path)