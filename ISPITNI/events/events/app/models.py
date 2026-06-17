from os import name

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Band(models.Model):
    name= models.CharField(max_length=50)
    country= models.CharField(max_length=50)
    year_formed= models.PositiveIntegerField()
    held_events = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Event(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    datetime = models.DateTimeField()
    bands= models.ManyToManyField(Band)
    poster = models.ImageField(upload_to='posters')
    outdoor = models.BooleanField(default='true')
    place = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name

