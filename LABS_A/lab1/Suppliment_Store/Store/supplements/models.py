from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=100)
    description = models.TextField()
    is_active= models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Company(models.Model):
    COMPANY_TYPES=[
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]
    name= models.CharField(max_length=100)
    founded_date= models.DateField()
    company_type = models.CharField(max_length=10,choices=COMPANY_TYPES)

    def __str__(self):
        return self.name

class Supplement (models.Model):
    name= models.CharField(max_length=100)
    manufacturer= models.ForeignKey(Company, on_delete=models.CASCADE)
    description= models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='supplements/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


