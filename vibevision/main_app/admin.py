from django.contrib import admin
from .models import User, Movie ,Genre, ShowTime, Booking, BookingSeat, Seat, Room
# Register your models here.

admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(ShowTime)
admin.site.register(Booking)
admin.site.register(BookingSeat)
admin.site.register(Seat)
admin.site.register(Room)


