from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class SystemUser(models.Model):
    ROLE_CHOICES = [
        ('recruiter', 'Recruiter'),
        ('applicant', 'Applicant'),
        ('inspector', 'Inspector')
    ]
    full_name = models.CharField(max_length=100)
    role = models.CharField(choices=ROLE_CHOICES, max_length=50)
    profile_photo = models.ImageField(upload_to='photos')
    date_of_birth = models.DateField()
    years_experience = models.PositiveIntegerField()
    phone = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class JobAd (models.Model):
    CATEGORY_CHOICES = [
        ('development','Development'),
        ('design', 'Design'),
        ('marketing', 'Marketing'),
        ('data', 'Data'),
        ('other', 'Other'),
    ]
    LEVEL_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),

    ]
    title = models.CharField(max_length=100)
    open_until = models.DateField()
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES)
    level = models.CharField(choices=LEVEL_CHOICES)
    recruiter = models.ForeignKey(SystemUser ,on_delete=models.CASCADE)

class Application (models.Model):
    job_ad = models.CharField(max_length=100)
    applicant = models.ForeignKey
    expected_salary = models.IntegerField()
    created_at= models.DateField()
    cv = models.FileField()
    applicant_note = models.TextField()
    recruiter_note = models.TextField()

class Interview (models.Model):
    job_ad = models.ForeignKey(JobAd , on_delete=models.CASCADE)
    applicant = models.ForeignKey(SystemUser, on_delete=models.CASCADE)
    scheduled_at = models.DateField()

