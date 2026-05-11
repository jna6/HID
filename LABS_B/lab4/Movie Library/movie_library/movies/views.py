from django.shortcuts import render, redirect

from .forms import MovieForm
from .models import Movie


# Create your views here.
def index(request):
    movies= Movie.objects.all()
    context={"movies":movies}
    return render(request,'movies/index.html',context)

def add_movie(request):
    if request.method=="POST":
        form = MovieForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form=MovieForm()
    return render(request,'movies/add_movie.html',{"form":form})