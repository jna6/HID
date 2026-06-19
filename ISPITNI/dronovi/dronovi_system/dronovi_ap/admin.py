
from django.contrib import admin
from django.db.models import Q
from django.utils import timezone

from .models import *
# Register your models here.

class DroneAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj:Drone = None):
        return Pilot.objects.filter(user = request.user, num_reservations__gt=3).exists()

class PilotAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser

class ReservationAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_authenticated and Pilot.objects.filter(user = request.user).exists()

    def save_model(self, request, obj, form, change):
        if not change:
            obj.main_pilot = Pilot.objects.filter(user = request.user).exists()
        super().save_model(request, obj, form,change)

    def has_change_permission(self, request, obj:Reservation = None):
        if obj is None:
            return True
        if obj.status != 'na_chekanje':
            return False
        pilot_qs = Pilot.objects.filter(user = request.user).first()
        if obj.main_pilot == pilot_qs:
            return True
        return PilotReservation.objects.filter(reservation = obj , pilot = pilot_qs).exists()

    def has_delete_permission(self, request, obj:Reservation = None):
        if obj is None:
            return True
        if obj.status != 'na_chekanje':
            return False
        pilots = PilotReservation.objects.filter(reservation = obj).exists()
        if obj.main_pilot.user == request.user and pilots == False:
            return True
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        today = timezone.now().date()
        pilot = Pilot.objects.filter(user = request.user)
        if pilot:
            return qs.filter(Q(main_pilot = pilot , status__in=['aktivna','na_chekanje'],date__gte=today) | Q(status__in=['zavrshena']))
        return qs.none()

admin.site.register(Drone,DroneAdmin)
admin.site.register(Pilot,PilotAdmin)
admin.site.register(Reservation,ReservationAdmin)
admin.site.register(PilotReservation)
