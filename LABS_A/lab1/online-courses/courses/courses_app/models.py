from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    is_popular = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Teacher (models.Model):
    EXPERIENCE_LEVELS =[
        ('BEGINNER','Beginner'),
        ('INTERMEDIATE','Intermediate'),
        ('EXPERT','Expert')
    ]
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    biography = models.TextField()
    experience_level = models.CharField(max_length=50, choices=EXPERIENCE_LEVELS)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course (models.Model):
    title = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    description = models.TextField()
    user =models.ForeignKey(User , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='courses_app')
    price = models.FloatField()
    availability= models.PositiveIntegerField()

    def __str__(self):
        return self.title


