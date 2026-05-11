from django.urls import path

from . import views

app_name = 'agency'
urlpatterns = [
    path('index/',views.index,name='index'),
    path('details/<int:pk>/',views.detail,name='details')
]