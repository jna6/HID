from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Guide(models.Model):
    user= models.OneToOneField(User , on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email= models.EmailField()

    def __str__(self):
        return self.full_name


class Travel(models.Model):
    destination = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    duration = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='photos')
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)

    def __str__(self):
        return self.destination
