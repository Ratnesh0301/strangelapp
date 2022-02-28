from distutils.command.upload import upload
from statistics import mode
from xml.parsers.expat import model
from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    referral = models.CharField(max_length=10)
    created_at = models.DateField(auto_now=True)
    last_modified = models.DateField(auto_now=True)
    is_strangel = models.BooleanField(default=0)
    image = models.ImageField(upload_to='./user_images/')

class Safepoints(models.Model):
    sp_name = models.CharField(max_length=100)
    sp_address = models.TextField()
    sp_number = models.CharField(max_length=20)
    sp_latitude = models.CharField(max_length=50)
    sp_longitude = models.CharField(max_length=50)
    sp_timings = models.TextField()
    sp_created_at = models.DateField(auto_now=True)
    last_modified = models.DateField(auto_now=True)
    sp_image = models.ImageField(upload_to='./sp_images/')



