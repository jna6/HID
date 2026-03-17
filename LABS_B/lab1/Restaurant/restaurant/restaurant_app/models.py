from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# Креирајте Django апликација за менаџирање на ресторани и нивни резервации. Секоја резервација се карактеризира со датум и време, број на гости, посебни барања (текст), ресторан, корисник кој ја направил резервацијата, статус на резервацијата (Потврдена, Во чекање, Откажана) и вкупна проценета цена. За секој ресторан се чуваат: име на ресторанот, адреса, краток опис, кујна (тип на храна), слика и максимален капацитет. За секој тип на кујна се чува: името на кујната, земја на потекло, кратко опишување и дали е моментално во тренд (boolean).

class Cuisine (models.Model):
    name= models.CharField(max_length=100)
    country= models.CharField(max_length=100)
    description = models.TextField()
    is_trendy= models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name= models.CharField(max_length=100)
    address =models.TextField()
    description = models.TextField()
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='restaurant/')
    capacity= models.IntegerField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('CONFIRMED', 'Confirmed'),
        ('PENDING', 'Pending'),
        ('CANCELLED', 'Cancelled'),
    ]
    date_time = models.DateTimeField()
    number_of_guests = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    status = models.CharField( choices=STATUS_CHOICES, default='PENDING')

    estimated_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Reservation for {self.restaurant} on {self.date_time}"