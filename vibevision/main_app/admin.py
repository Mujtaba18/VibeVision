from django.contrib import admin
from .models import User, Movie ,Genre
# Register your models here.

admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Genre)

