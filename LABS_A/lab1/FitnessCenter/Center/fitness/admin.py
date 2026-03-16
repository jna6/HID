from django.contrib import admin

from .models import Category, Instructor, Training

# Register your models here.
admin.site.register(Category)
admin.site.register(Instructor)

class TrainingAdmin(admin.ModelAdmin):
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user= request.user
        super().save_model(request, obj, form, change)

admin.site.register(Training,TrainingAdmin)


