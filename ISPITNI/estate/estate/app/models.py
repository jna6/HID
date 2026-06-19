from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Estate (models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    area = models.PositiveIntegerField()
    date = models.DateField()
    photo = models.ImageField(upload_to='photos')
    price = models.IntegerField()
    is_reserved = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Agent (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    link = models.CharField(max_length=100)
    sales = models.PositiveIntegerField()
    email = models.EmailField()
    def __str__(self):
        return self.full_name

# M :N
class AgentEstate(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    estate = models.ForeignKey(Estate,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.agent.full_name} - {self.estate.name}"

class Characteristic(models.Model):
    price = models.IntegerField()
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class EstateCharacteristics (models.Model):
    estate = models.ForeignKey(Estate,on_delete=models.CASCADE)
    characteristic = models.ForeignKey(Characteristic,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.estate.name} - {self.characteristic.name} "