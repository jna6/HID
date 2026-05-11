from django.db import models

# Create your models here.
class Movie(models.Model):
    GENRES=[
        ('ACTION', 'Action'),
        ('COMEDY', 'Comedy'),
        ('DRAMA', 'Drama'),
        ('SCIENCE FICTION', 'Science Fiction'),
        ('HORROR', 'Horror'),
        ('MUSICAL', 'Musical'),
        ('DOCUMENTARY', 'Documentary'),
    ]
    FORMATS=[
        ('DVD', 'DVD'),
        ('BLU-RAY', 'Blu-ray'),
        ('DIGITAL', 'Digital'),
    ]

    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='posters/')
    imbd_code = models.FloatField()
    year = models.IntegerField()
    duration= models.IntegerField()
    genre= models.CharField(max_length=100, choices=GENRES)
    format=models.CharField(max_length=100, choices=FORMATS)
    rental_price=models.DecimalField(max_digits=5, decimal_places=2)

    production_company=models.ForeignKey('Production', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Production(models.Model):
    name=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    founded_year=models.IntegerField()
    website=models.URLField()

    def __str__(self):
        return self.name