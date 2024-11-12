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
from .forms import CustomUserCreationForm
from .forms import UserProfileForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('<h1>Hello Cat About</h1>')
    return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = CustomUserCreationForm(request.POST, request.FILES)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = CustomUserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def profile(request):
  user = request.user
  return render(request, 'profile/profile.html', {'user': user})

def profile_update(request):
  user = request.user
  if request.method == 'POST':
     form = UserProfileForm(request.POST, request.FILES, instance=user)
     if form.is_valid():
        form.save()
        return redirect('profile')
     else:
      error_message = 'Invalid update profile - try again'

  form = UserProfileForm(instance=user)

  context = {
        'form': form,
        'user': user,
  }

  return render(request, 'profile/profile_edit.html', context)

# Movie create view
class MovieCreate(LoginRequiredMixin,  CreateView):
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
            'status'
        ]
    success_url = '/movies/'  

    def form_valid(self, form):
        form.instance.user = self.request.user  # Attach the current user to the movie
        return super().form_valid(form)

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

class MovieDetail(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'

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
def seat_list(request):
    return render(request, 'seats/seat_list.html')

# Seat list view 

class SeatList(ListView):
    model = Seat
    template_name = 'seats/seat_list.html'
    
# Seat Create View
class SeatCreate( CreateView):
    model = Seat
    template_name = 'seats/seat_form.html'
    fields = ['seat_code', 'seat_type', 'price']
    success_url = '/seat/'  

# Seat Update View
class SeatUpdate( UpdateView):
    model = Seat
    template_name = 'seats/seat_form.html'
    fields = ['seat_code', 'seat_type', 'price']
    success_url = '/seat/'  

# Seat Delete View
class SeatDelete(DeleteView):
    model = Seat
    template_name = 'seats/seat_confirm_delete.html'
    success_url = '/seat/'  

## ----------------------------------- BookingSeat


## ----------------------------------- Booking

