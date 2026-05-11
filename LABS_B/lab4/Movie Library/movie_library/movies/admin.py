from django.contrib import admin

from .models import (Movie, Production)

# Register your models here.
admin.site.register(Movie)
admin.site.register(Production)