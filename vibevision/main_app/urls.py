from django.contrib import admin
# Add the include function to the import
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    ## Movie
    path('movies/', views.MovieList.as_view(), name='movie_list'),
    path('movies/create/', views.MovieCreate.as_view(), name='movie_create'),
    path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movie_update'),
    path('movies/<int:pk>/delete/', views.MovieDelete.as_view(), name='movie_delete'),

    ## Room
    path('rooms/', views.RoomList.as_view(), name='room_list'),
    path('rooms/create/', views.RoomCreate.as_view(), name='room_create'),
    path('rooms/<int:pk>/update/', views.RoomUpdate.as_view(), name='room_update'),
    path('rooms/<int:pk>/delete/', views.RoomDelete.as_view(), name='room_delete'),

    ## Showtime
    path('showtimes/', views.ShowTimeList.as_view(), name='showtime_list'),
    path('showtimes/create/', views.ShowTimeCreate.as_view(), name='showtime_create'),
    path('showtimes/<int:pk>/update/', views.ShowTimeUpdate.as_view(), name='showtime_update'),
    path('showtimes/<int:pk>/delete/', views.ShowTimeDelete.as_view(), name='showtime_delete'),

    ## Seat


    ## BookingSeat


    ## Booking

]