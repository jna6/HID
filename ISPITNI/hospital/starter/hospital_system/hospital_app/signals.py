# Define your signal receivers here.
from django.utils.timezone import now
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver

from .models import Appointment, Patient


@receiver(pre_save,sender=Appointment)
def appointment_status_adjustment(sender,instance,**kwargs):
    if instance.status =='completed' and instance.datetime > now():
        instance.status ='scheduled'
    if instance.status =='scheduled' and instance.datetime < now():
        instance.status ='completed'

    if instance.pk is None and instance.patient_id is not None:
        doctor= instance.responsible_doctor
        patient_institution = instance.patient.institution
        patient_ids = (
            Appointment.objects.filter(
                responsible_doctor=doctor,
                patient__institution= patient_institution,
            )
            .values_list('patient_id',flat=True)
            .distinct()
        )
        if len(patient_ids)>=3:
            instance.note = f"High workload with patients from institution " f"{patient_institution}."


@receiver(pre_delete,sender=Patient)
def cleanup_appointments (sender,instance,**kwargs):
    for appt in Appointment.objects.filter(patient=instance):
        if appt.status=='scheduled':
            appt.delete()
        elif appt.status=='in_progress':
            appt.note = "Patient record missing – appointment preserved for audit purposes"
            appt.save()