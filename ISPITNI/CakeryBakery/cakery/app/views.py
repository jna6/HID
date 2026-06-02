from django.shortcuts import render, redirect

# Create your views here.

from .models import *
from .forms import CakeForm
def index(request):
    cakes=Cake.objects.all()
    context={'cakes':cakes}
    return render(request,'index.html',context)

def add_cake(request):
    if request.method=='POST':
        baker= Baker.objects.filter(user=request.user).first()
        form= CakeForm(request.POST,request.FILES)
        if form.is_valid():
            cake= form.save(commit=False)
            cake.baker = baker
            cake.save()
            return redirect('index')
    form=CakeForm()
    context={'form':form}
    return render(request,'add.html',context)