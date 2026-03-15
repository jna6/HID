from django.contrib import admin

from .models import Genre, Author, Book

# Register your models here.

admin.site.register(Genre)
admin.site.register(Author)

class BookAdmin(admin.ModelAdmin):
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)