from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('movies/add/', views.add_movie , name='add_movie'),
]