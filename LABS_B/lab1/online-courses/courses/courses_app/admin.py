from django.contrib import admin
from .models import Category, Teacher,Course

# Register your models here.

admin.site.register(Category)
admin.site.register(Teacher)

class CourseAdmin (admin.ModelAdmin):
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user= request.user
        super().save_model(request, obj, form, change)

admin.site.register(Course, CourseAdmin)