from django.contrib import admin

from .models import Cuisine, Restaurant, Reservation

# Register your models here.

admin.site.register(Cuisine)
admin.site.register(Restaurant)

class ReservationAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request,obj, form, change)

admin.site.register(Reservation,ReservationAdmin)