from django.contrib import admin
from django.utils import timezone

# Register your models here.
from .models import *

class AgentEstateInline(admin.TabularInline):
    model = AgentEstate
    extra = 0

class EstateCharacteristicsInline(admin.TabularInline):
    model = EstateCharacteristics
    extra = 0

class AgentAdmin (admin.ModelAdmin):
    list_display = ['full_name']
    def has_add_permission(self, request):
        return request.user.is_superuser

class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ['name']

    def has_add_permission(self, request):
        return request.user.is_superuser

class EstateAdmin(admin.ModelAdmin):
    list_display = ['name','location','area']
    def save_model(self, request, obj, form, change):
        if not change:
            agent = Agent.objects.filter(user = request.user).first()
            AgentEstate.objects.create(estate=obj, agent= agent)
        super().save_model(request, obj, form, change)
    def has_change_permission(self, request, obj = None):
        return obj and AgentEstate.objects.filter(estate=obj , agent__user = request.user).exists()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        today = timezone.now().date()

        if request.user.is_superuser:
            return qs.filter(date = today)
        return qs

    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return not EstateCharacteristics.objects.filter(estate=obj).exists()


