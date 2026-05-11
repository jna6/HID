from django.db import models

# Create your models here.

class Agency(models.Model):
    name= models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    year_founded = models.IntegerField()
    website = models.URLField()

    def __str__(self):
        return self.name

class Property(models.Model):
    PROPERTY_TYPES = [
        ('HOUSE', 'House'),
        ('APARTMENT', 'Apartment'),
        ('LAND', 'Land'),
        ('COMMERCIAL', 'Commercial'),
        ('STUDIO', 'Studio'),
        ('VILLA', 'Villa'),
        ('OFFICE', 'Office'),
    ]
    STATUS_CHOICES = [
        ('For Sale', 'Sale'),
        ('For Rent', 'Rent'),
        ('Sold', 'Sold'),
        ('Rented','Rented')
    ]
    title = models.CharField(max_length=200)
    image= models.ImageField(upload_to='images/')
    location = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    area = models.FloatField()
    rooms = models.IntegerField()
    floor = models.IntegerField()
    build_year = models.IntegerField()

    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    agency = models.ForeignKey('Agency', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
