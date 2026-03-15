from django.contrib import admin
from .models import Category, Company, Supplement


admin.site.register(Category)
admin.site.register(Company)


class SupplementAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Supplement, SupplementAdmin)