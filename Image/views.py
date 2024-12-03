from django.shortcuts import render
from django.http import JsonResponse
from . import forms, models
from django.http import HttpResponseRedirect,HttpResponseServerError
# Create your views here.

def image_upload(request):
    if request.method == 'POST':
    #     form = forms.ImageForm(request.POST)

    #     if form.is_valid(): 
    #         instance = form.save(commit=False)
    #         instance.save()
    #         return HttpResponseRedirect("/")
    #     else:
    #             return JsonResponse({'error': 'Form is not valid.'}, status=400)
    # else:
    #     form = forms.ImageForm(data=request.POST)
        pic = models.image_details()

        pic.profile_pic = request.POST.get("profile_pic")
        pic.save()
        return HttpResponseRedirect("show")
    return render(request, "Image/image.html")

def show_image(request):
    all = models.image_details.objects.all()   
    return render(request, "Image/show.html", {'all':all})

from django.http import HttpResponse
def hotel_image_view(request):
 
    if request.method == 'POST':
        form = forms.HotelForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('success')
    else:
        form = forms.HotelForm()
    return render(request, 'Image/hotel.html', {'form': form})
 
def show_hotel(request):
    all = models.Hotel.objects.all()   
    return render(request, "Image/show-hotel.html", {'all':all})