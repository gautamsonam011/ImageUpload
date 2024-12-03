from django.db import models

# Create your models here.

class image_details(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics')


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')