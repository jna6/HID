from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Doctor (models.Model):
    SPECIALTY_CHOICES = [
        ('cardiologist','Cardiologist'),
        ('dermatologist','Dermatologist'),
        ('neurologist','Neurologist')
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,

    blank=True)
    full_name = models.CharField(max_length=100)
    specialty = models.CharField(choices=SPECIALTY_CHOICES,max_length=100)
    image = models.ImageField(upload_to='doctors/')
    institution = models.CharField(max_length=100)
    completed_appointments=models.PositiveIntegerField(default=0)
    email = models.EmailField()
    phone= models.CharField(max_length=20)

    def __str__(self):
        return self.full_name

class Patient (models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    full_name = models.CharField(max_length=100)
    birth_date= models.DateField()
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    email = models.EmailField()
    institution = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.full_name

class Appointment (models.Model):
    TYPE_CHOICES = [
        ('cardiology','Cardiology'),
        ('dermatology', 'Dermatology'),
        ('neurology', 'Neurology'),
    ]
    STATUS_CHOICES=[
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
    ]
    appointment_type = models.CharField(choices=TYPE_CHOICES,max_length=20,null=True,blank=True)
    description = models.TextField()
    status = models.CharField(choices= STATUS_CHOICES,max_length=20,default='scheduled')
    datetime = models.DateTimeField()
    note = models.TextField(blank=True,null=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL,null=True,related_name='appointments')
    responsible_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='responsible_appointments')

    def __str__(self):
        return f"{self.patient} {self.datetime} {self.responsible_doctor}"

class AppointmentAssignment(models.Model):
    appointment = models.ForeignKey(Appointment,on_delete=models.CASCADE,null=True,blank=True)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        unique_together =('appointment', 'doctor')
    def __str__(self):
        return f"{self.doctor.full_name}  assisting {self.appointment}"