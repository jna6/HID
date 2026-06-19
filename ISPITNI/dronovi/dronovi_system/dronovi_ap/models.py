from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Drone (models.Model):
    TYPE_CHOICES=[
        ('kinematski','Kinematski'),
        ('FPV','FPV'),
        ('industriski','Industriski'),
    ]
    STATUS_CHOICES=[
        ('dostapen','Dostapen'),
        ('rezerviran', 'Rezerviran'),
        ('na_servis', 'Na servis'),

    ]
    serial_num = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    type= models.CharField(choices=TYPE_CHOICES,max_length=50)
    photo = models.ImageField(upload_to='photos')
    status = models.CharField(choices=STATUS_CHOICES,max_length=50)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.serial_num

class Pilot (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name= models.CharField(max_length=100)
    email = models.EmailField()
    num_reservations = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

class Reservation (models.Model):
    TERMIN_CHOICES=[
        ('utro','Utro'),
         ('popladne', 'Popladne'),
         ('vecher', 'Vecher'),
    ]
    STATUS_CHOICES = [
        ('na_chekanje', 'Na chekanje'),
        ('aktivna', 'Aktivna'),
        ('zavrshena', 'Zavrshena'),
    ]
    date= models.DateField()
    termin = models.CharField(choices=TERMIN_CHOICES,max_length=50)
    main_pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES,max_length=50)
    note= models.TextField()
    code = models.CharField(max_length=100)
    drone = models.ForeignKey(Drone,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('drone','date','termin')
    def __str__(self):
        return f"{self.drone} {self.date} {self.termin}"

class PilotReservation(models.Model):
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation,on_delete=models.CASCADE)








