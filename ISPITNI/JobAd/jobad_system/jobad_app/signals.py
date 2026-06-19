from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import *


@receiver (post_save,sender=Interview)
def create_interview(sender, instance, created, **kwargs):
    if created:
        Application.objects.filter(job_ad = instance.job_ad).exclude(applicant= instance.applicant).update(recruiter_note ="THANK YOU")

@receiver(pre_save,sender=JobAd)
def delete_applications (sender,instance,**kwargs):
    if instance.pk:
        Application.objects.filter(job_ad= instance.job_ad).delete()