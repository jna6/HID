from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Baker(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} {self.surname}"

class Cake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField()
    weight = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='cakes/')
    baker= models.ForeignKey(Baker, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

