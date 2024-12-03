from django.shortcuts import render, redirect
from CrudOperation import models
# Create your views here.

def index_page(request):
    if request.method == 'POST':

        std_roll = request.POST.get('std_roll')
        std_name = request.POST.get('std_name')
        std_email = request.POST.get('std_email')
        std_address = request.POST.get('std_address')

        s = models.Student()

        s.roll = std_roll
        s.name = std_name
        s.email = std_email
        s.address = std_address

        s.save()
        return redirect('home')  
    return render(request, "CrudOperation/index.html",{})

# def update_std(request, pk):
#     std = models.Student.objects.get(id=pk)
#     return render(request, "CrudOperation/update.html", {'std':std})

def do_update(request,pk):
    std = models.Student.objects.get(id=pk)
    if request.method == 'POST':
        std_roll = request.POST.get('std_roll')
        std_name = request.POST.get('std_name')
        std_email = request.POST.get('std_email')
        std_address = request.POST.get('std_address')

        print("======>", std)
        std.roll = std_roll
        std.name = std_name
        std.email = std_email
        std.address = std_address
        std.save()
        
        return redirect('/home')
    return render(request, "CrudOperation/update.html", {'std':std})


def home_page(request):
    all = models.Student.objects.all()
    return render(request, "CrudOperation/home.html", {'all':all})

def delete_std(request, pk):
    s = models.Student.objects.get(id=pk)
    s.delete()
    return redirect('home')