from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie, Room, ShowTime, Seat, BookingSeat, Booking, User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 
# Signup - Signin - Authentication
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Authorization
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('<h1>Hello Cat About</h1>')
    return render(request, 'about.html')

# Add new view
## ----------------------------------- Movie

# Movie create view
class MovieCreate( CreateView):
    model = Movie
    template_name = 'movies/movie_form.html'
    fields = [
            'title',
            'description',
            'duration',
            'genres', 
            'movie_image', 
            'rating',
            'release_date',
            'language',
            'subtitle',
            'trailer_url',
            'rating',
            'age_restriction',
            
        ]
    success_url = '/movies/'  

# Movie list view 

class MovieList(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    

#  movie delete view 
class MovieDelete(DeleteView):
    model= Movie
    template_name = 'movies/movie_confirm_delete.html'
    success_url = '/movies/'  

#  movie update view 
class MovieUpdate(UpdateView):
    model= Movie
    fields ='__all__'
    template_name = 'movies/movie_form.html'
    success_url = '/movies/'  

## ----------------------------------- Room

# Room list view 

class RoomList(ListView):
    model = Room
    template_name = 'rooms/room_list.html'
    
# Room Create View
class RoomCreate( CreateView):
    model = Room
    template_name = 'rooms/room_form.html'
    fields = ['name', 'capacity']
    success_url = '/rooms/'  

# Room Update View
class RoomUpdate( UpdateView):
    model = Room
    template_name = 'rooms/room_form.html'
    fields = ['name', 'capacity']
    success_url = '/rooms/'  

# Room Delete View
class RoomDelete(DeleteView):
    model = Room
    template_name = 'rooms/room_confirm_delete.html'
    success_url = '/rooms/'  


## ----------------------------------- Showtime

# ShowTime List View
class ShowTimeList( ListView):
    model = ShowTime
    template_name = 'showtimes/showtime_list.html'

# ShowTime Create View
class ShowTimeCreate(CreateView):
    model = ShowTime
    template_name = 'showtimes/showtime_form.html'
    fields = ['movie', 'room', 'show_time']
    success_url = '/showtimes/' 

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.all()
        context['rooms'] = Room.objects.all()
        return context
    

# ShowTime Update View
class ShowTimeUpdate( UpdateView):
    model = ShowTime
    template_name = 'showtimes/showtime_form.html'
    fields = ['movie', 'room', 'show_time']
    success_url = '/showtimes/'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.all()
        context['rooms'] = Room.objects.all()
        return context

# ShowTime Delete View
class ShowTimeDelete( DeleteView):
    model = ShowTime
    template_name = 'showtimes/showtime_confirm_delete.html'
    success_url = '/showtimes/' 


## ----------------------------------- Seat


## ----------------------------------- BookingSeat


## ----------------------------------- Booking

