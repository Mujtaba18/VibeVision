from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models


AGE_RE =(
       ( 'G', 'General Audience'),
       ('PG', 'Parental Guidance'),
       ('PG-13', 'Parents Strongly Cautioned'),
       ('R', 'Restricted'),
       ('NC-17', 'Adults Only'))

LANGUAGES = (
    ('Arabic','ARB'),
    ( 'English','ENG',),
    ( 'Hindi', 'HIN')
)



# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'admin'),
        ('user', 'user'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    image = models.ImageField(upload_to='main_app/static/uploads/user_images/', null=True, blank=True, default="")

    def __str__(self):
        return self.username

class Room(models.Model):
    name = models.CharField(max_length=50) 
    capacity = models.PositiveIntegerField()  # Total number of seats in the room

    def __str__(self):
            return self.name
    
class Seat(models.Model):
    SEAT_TYPES = [
        ('VIP', 'VIP'),
        ('Deluxe', 'Deluxe'),
        ('Standard', 'Standard'),
    ]
    
    seat_code = models.CharField(max_length=10, unique=True)  # e.g., "A1", "B2"
    seat_type = models.CharField(max_length=10, choices=SEAT_TYPES, default='Standard')  # VIP, Deluxe, Standard
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.seat_code} ({self.get_seat_type_display()}) - ${self.price}"
    
class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField() 
    subtitle = models.CharField(max_length=50, choices=LANGUAGES , default=LANGUAGES[0][1])
    duration = models.CharField(max_length=50)
    release_date = models.DateField()
    language = models.CharField(max_length=50, choices=LANGUAGES , default=LANGUAGES[0][1])
    trailer_url = models.CharField(max_length=255, default="None")
    movie_image = models.ImageField(upload_to='main_app/static/uploads/movie_images', null=True, blank=True )
    rating = models.DecimalField(decimal_places=1, default=0, max_digits=3)  
    age_restriction = models.CharField(max_length=150, default=AGE_RE[0][0], choices=AGE_RE)  
    genres = models.ManyToManyField(Genre, blank=True)
    def __str__(self):
        return self.title
    
class ShowTime(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='showtimes')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    
    class Meta:
        unique_together = ('movie', 'room', 'start_time')
    
    def __str__(self):
        return f"{self.movie.title} in {self.room.name} at {self.start_time}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    showtime = models.ForeignKey(ShowTime, on_delete=models.CASCADE, related_name='bookings')
    seats = models.ManyToManyField(Seat, through='BookingSeat', related_name='bookings')
    booking_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Booking by {self.user.username} for {self.movie.title} in {self.room.name} at {self.showtime.start_time}"

class BookingSeat(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('booking', 'seat')

    def __str__(self):
        return f"Seat {self.seat.seat_code} for booking {self.booking}"

