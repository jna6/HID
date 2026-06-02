import random

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.db.models import Count, Sum

from .models import Baker,Cake


# Register your models here.

class BakerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser
    def has_change_permission(self, request, obj = None):
        return request.user.is_superuser
    def has_delete_permission(self, request, obj = None):
        return request.user.is_superuser
    def get_queryset(self, request):
        qs= super().get_queryset(request)
        if request.user.is_superuser:
            return qs.annotate(cake_count=Count('cake')).filter(cake_count__lt=5)
        return qs
    def delete_model(self, request, obj:Baker):
        bakers = list(Baker.objects.exclude(id=obj.id))
        for cake in obj.cake_set.all():
            cake.baker = random.choice(bakers)
            cake.save()
        obj.delete()

class CakeAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj:Cake = None):
        return obj and request.user==obj.baker.user
    def has_view_permission(self, request, obj = None):
        return request.user is not None
    def save_model(self, request, obj:Cake, form, change):
        if not request.user.is_superuser:
            obj.baker = Baker.objects.get(user=request.user)
        baker = obj.baker
        cakes=Cake.objects.filter(baker=baker).exclude(id=obj.id)
        if cakes.count()>10:
            raise ValidationError("Cannot have more than 10 cakes per baker")
        total_price = cakes.aggregate(total_price=Sum('price'))['total_price'] or 0
        if total_price +obj.price > 10000:
            raise ValidationError("Total price cannot exceed 10000")
        return super().save_model(request, obj, form, change)

admin.site.register(Baker,BakerAdmin)
admin.site.register(Cake,CakeAdmin)