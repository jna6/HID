
from django.shortcuts import render, get_object_or_404

from .models import Property


# Create your views here.

def index(request):
    properties = Property.objects.all()

    context = {'properties': properties}
    return render(request,'agency/index.html',context)

def detail(request,pk):
    property=get_object_or_404(Property,pk=pk)
    context={'property':property}
    return render(request,'agency/details.html',context)