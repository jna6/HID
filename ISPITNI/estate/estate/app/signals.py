from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

from .models import *

@receiver(pre_save, sender=Estate)
def my_handler(sender, instance, **kwargs):
    old_instance = Estate.objects.filter(id = instance.id).first()
    if old_instance:
        if instance.is_sold != old_instance.is_sold:
            array = AgentEstate.objects.filter(estate = old_instance).all()
            for a in array:
                a.agent.sales += 1
                a.agent.save()