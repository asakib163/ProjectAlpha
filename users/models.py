from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')
    blood_group = models.CharField(max_length=50)
    marrital_status = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    #gender = models.CharField(max_length=20)
    #religion = models.CharField(max_length=20)
    #relation = models.CharField(max_length=50)
    #contact_no = models.CharField(max_length=20)


    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self):
    #     super().save()
    #     img = Image.open(self.image.path)
    #     if img.height >500 or img.width>500:
    #         output_size = (500,500)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)