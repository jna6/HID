import random

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from travel.app.models import Guide, Travel


@receiver(pre_delete,sender=Guide)
def reasign(sender, instance,**kwargs):
    other_guides = Guide.objects.exclude(id = instance.id).all()
    destinations = Travel.objects.filter(guide=instance)
    for d in destinations:
        new_guide = random.choice(other_guides)
        d.guide = new_guide
        d.save()