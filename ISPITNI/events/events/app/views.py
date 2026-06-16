from django.shortcuts import render, redirect

from .models import Event, Band
from .forms import EventForm

# Create your views here.

def index(request):
    events = Event.objects.filter(creator=request.user)
    return render(request, 'index.html',{'events':events})

def add_event(request):

    if request.method == "POST":
        form = EventForm(
            request.POST,
            request.FILES
        )
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.save()
            band_names = form.cleaned_data['bands']
            names = [
                x.strip()
                for x in band_names.split(',')
            ]
            for name in names:
                try:
                    band = Band.objects.get(name=name)
                    event.bands.add(band)
                except Band.DoesNotExist:
                    pass
            return redirect('index')
    else:
        form = EventForm()
    return render(request,'add_event.html',{'form': form})