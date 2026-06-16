from django.contrib import admin

# Register your models here.
from .models import Band,Event
@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = 'name','country',
    def has_add_permission(self, request):
        return request.user.is_superuser

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = 'name','datetime'
    def has_add_permission(self, request):
        return request.user.is_superuser

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj:Event = None):
        if obj is None:
            return True
        return request.user== obj.creator and obj.bands.count()==0

    def has_delete_permission(self, request, obj:Event = None):
        if obj is None:
            return True
        return request.user == obj.creator and obj.bands.count() == 0
