from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from .forms import *

def index(request):
    destinations = Travel.objects.all()
    context = {'destinations':destinations}
    render(request,'index.html',context)

def add(request):
    if request.method =='POST':
        form = TravelForm(request.POST)
        if form.is_valid:
            travel = form.save()
            travel.guide= Guide.objects.get(user = request.user)
            travel.save()
            return redirect('index')
    form = TravelForm
    context = {'form':form}
    return render(request,'add.html', context)