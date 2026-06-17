import random
from functools import total_ordering

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.db.models import Count, Sum

from .models import Guide,Travel


# Register your models here.

class GuideAdmin (admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser
    def has_change_permission(self, request, obj = None):
        return request.user.is_superuser
    def has_delete_permission(self, request, obj = None):
        return request.user.is_superuser

class TravelAdmin (admin.ModelAdmin):
    def has_change_permission(self, request, obj:Travel = None):
        return obj and obj.guide == request.user

    def save_model(self, request, obj:Travel, form, change):
        guide = Guide.objects.filter(user=request.user).first()
        destinations = Travel.objects.filter(guide=guide).all()
        total = 0
        for destination in destinations:
            total+= destination.price

        if not change:
            if destinations.count() >= 5:
                raise ValidationError("Cannot add more than 5 destinations")
            if Travel.objects.filter(destination = obj.destination).exists():
                raise ValidationError("Destination already exists")
            if total + obj.price > 50000:
                raise ValidationError ("Total price cannot exceed 50000")
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.annotate(travel_count = Count('destination')).filter(travel_count__lt=3)
        return qs