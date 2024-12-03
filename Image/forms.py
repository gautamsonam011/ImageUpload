from django import forms
from django.contrib.auth.models import User
from . import models

class ImageForm(forms.ModelForm):
    class Meta:
        model=models.image_details
        fields=['profile_pic']

class HotelForm(forms.ModelForm):
 
    class Meta:
        model = models.Hotel
        fields = ['name', 'hotel_Main_Img']
     