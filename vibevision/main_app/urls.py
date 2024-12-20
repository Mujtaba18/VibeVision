from django.contrib import admin
# Add the include function to the import
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),

    ## Movie
    path('movies/', views.MovieList.as_view(), name='movie_list'),
    path('movies/create/', views.MovieCreate.as_view(), name='movie_create'),
    path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movie_update'),
    path('movies/<int:pk>/delete/', views.MovieDelete.as_view(), name='movie_delete'),
    path('movies/detail/<int:pk>/', views.MovieDetail.as_view(), name='movie_detail' ),

    ## Room
    path('rooms/', views.RoomList.as_view(), name='room_list'),
    path('rooms/create/', views.RoomCreate.as_view(), name='room_create'),
    path('rooms/<int:pk>/update/', views.RoomUpdate.as_view(), name='room_update'),
    path('rooms/<int:pk>/delete/', views.RoomDelete.as_view(), name='room_delete'),

    ## Showtime
    path('showtimes/', views.ShowTimeList.as_view(), name='showtime_list'),
    path('showtimes/create/', views.ShowTimeCreate.as_view(), name='showtime_create'),

    path('showtime/<int:pk>/update/<int:movie_id>/', views.ShowTimeUpdate.as_view(), name='showtime_update'),
    path('showtimes/<int:pk>/delete/', views.ShowTimeDelete.as_view(), name='showtime_delete'),
    path('showtime/search', views.search ,name='showtime_search'),
    ## Seat
    path('seat/', views.SeatList.as_view(), name='seat_list'),
    path('seat/create/', views.SeatCreate.as_view(), name='seat_create'),
    path('seat/<int:pk>/update/', views.SeatUpdate.as_view(), name='seat_update'),
    path('seat/<int:pk>/delete/', views.SeatDelete.as_view(), name='seat_delete'),

    ## BookingSeat


    ## Booking
    path('booking/', views.BookingList.as_view(), name='booking_list'),
    path('booking/<int:pk>/delete/', views.BookingDelete.as_view(), name='booking_delete'),
    path('booking/create/<int:showtime_id>/', views.BookingCreateView.as_view(), name='booking_create'),
    path('booking/detail/<int:booking_id>/', views.booking_detail, name='booking_detail' ),
]