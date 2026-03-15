from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE

# Create your models here.
class Genre (models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    is_popular = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Author (models.Model):
    EXPERIENCE_LEVELS =[
        ('BEGINNER','Beginner'),
        ('PROFESSIONAL', 'Professional'),
        ('ESTABLISHED', 'Established'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.TextField()
    experience_level = models.CharField(max_length=50 ,choices=EXPERIENCE_LEVELS)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book (models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=CASCADE)
    summary= models.TextField()
    genre = models.ForeignKey(Genre,on_delete=CASCADE)
    user= models.ForeignKey(User,on_delete=CASCADE)
    cover_img= models.ImageField(upload_to='books/')
    price= models.FloatField()
    available_copies = models.IntegerField()

    def __str__(self):
        return self.title