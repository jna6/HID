from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    is_popular = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Instructor(models.Model):
    firs_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.TextField()
    EXPERIENCE_LEVELS=[
        ('BEGINNER', 'Beginner'),
        ('CERTIFIED', 'Certified'),
        ('PROFESSIONAL', 'Professional'),
    ]
    experience_level= models.CharField(max_length=50, choices=EXPERIENCE_LEVELS)

    def __str__(self):
        return f"{self.firs_name} {self.last_name}"

class Training(models.Model):
    title = models.CharField(max_length=50)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    description= models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='fitness/')
    price =models.FloatField(max_length=10)
    availability= models.PositiveIntegerField()

    def __str__(self):
        return self.title
