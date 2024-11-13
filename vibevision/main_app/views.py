from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Room, ShowTime, Seat, BookingSeat, Booking, User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 
# Signup - Signin - Authentication
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Authorization
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import CustomUserCreationForm
from .forms import UserProfileForm
# Create your views here.

def home(request):
    showtimes_now = ShowTime.objects.filter(movie__status='Now Showing')  
    movies = Movie.objects.all()
    return render(request, 'home.html', {'showtimesNow': showtimes_now, 'movies': movies})

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        showtimes = ShowTime.objects.filter(movie=self.object).order_by('show_time')
        grouped_showtimes = {}
        for showtime in showtimes:
            date = showtime.show_time.date()
            if date not in grouped_showtimes:
                grouped_showtimes[date] = []
            grouped_showtimes[date].append(showtime)
        
        context['grouped_showtimes'] = grouped_showtimes
        return context

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

def search(request):
    query = request.GET.get('search')  # Get the search query from the request
    results = []
    movies = []
    
    if query:
        # Search for showtimes by movie title
        results = ShowTime.objects.filter(movie__title__icontains=query)
        movies = Movie.objects.filter(title__icontains=query)

    return render(request, 'showtimes/search.html', {'results': results, 'query': query, 'movies': movies})

# ShowTime List View
class ShowTimeList( ListView):
    model = ShowTime
    template_name = 'showtimes/showtime_list.html'

# ShowTime Create View
class ShowTimeCreate(CreateView):
    model = ShowTime
    template_name = 'showtimes/showtime_form.html'
    fields = [ 'room', 'show_time']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.all()   # send movies data to templates
        context['rooms'] = Room.objects.all()    # send rooms data to templates
        
        movie_id = self.request.GET.get('movie_id')
        if movie_id:
            context['selected_movie_id'] = movie_id 
        
        return context

    def form_valid(self, form):
        movie_id = self.request.GET.get('movie_id')  # Get movie_id from query params
        if movie_id:
            form.instance.movie_id = movie_id  
        return super().form_valid(form)

    success_url = '/showtimes/' 

    

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
        # Set selected_movie_id for the edit form
        context['selected_movie_id'] = self.object.movie.id
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
class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    fields = []
    template_name = 'bookings/booking_form.html'

    def form_valid(self, form):
        # Retrieve the selected seats from the form data
        selected_seat_ids = self.request.POST.get('selected_seats', '').split(',')

        # Handle the case where no seats are selected
        if not selected_seat_ids or selected_seat_ids == ['']:
            form.add_error(None, "Please select at least one seat.")
            return self.form_invalid(form)

        # Ensure that selected_seat_ids is a list of strings, not bytes
        selected_seat_ids = [seat_id for seat_id in selected_seat_ids if seat_id]

        # Process the rest of the form (movie, showtime, etc.)
        showtime_id = self.kwargs['showtime_id']
        showtime = get_object_or_404(ShowTime, id=showtime_id)

        form.instance.user = self.request.user
        form.instance.movie = showtime.movie
        form.instance.room = showtime.room
        form.instance.showtime = showtime

        # Save the booking instance first
        response = super().form_valid(form)

        # Link selected seats with the booking
        selected_seats = Seat.objects.filter(id__in=selected_seat_ids)
        for seat in selected_seats:
            BookingSeat.objects.create(booking=form.instance, seat=seat)

        # Success message
        messages.success(self.request, f"Successfully booked {len(selected_seats)} seats!")

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get showtime object from the URL
        showtime_id = self.kwargs['showtime_id']
        showtime = ShowTime.objects.get(id=showtime_id)
        context['showtime'] = showtime
        context['movie'] = showtime.movie

        # Get all seats (including booked ones)
        all_seats = Seat.objects.all()
        booked_seats = BookingSeat.objects.filter(booking__showtime=showtime).values_list('seat_id', flat=True)

        context['all_seats'] = all_seats
        context['booked_seats'] = set(booked_seats)  # Pass booked seat IDs to the template
        return context

    def get_success_url(self):
        movie_id = self.object.movie.id
        url = reverse('movie_detail', kwargs={'pk': movie_id})
        return url

# Booking List View
class BookingList( ListView):
    model = Booking
    template_name = 'bookings/booking_list.html'

#  Booking delete view 
class BookingDelete(DeleteView):
    model= Booking
    template_name = 'bookings/booking_confirm_delete.html'
    success_url = '/booking/'  

#  Booking details view 
class booking_detail(DetailView):
    model = Booking
    template_name = 'bookings/booking_detail.html'

def booking_detail(request, booking_id):
    # Retrieve the booking object using booking_id
    booking = get_object_or_404(Booking, id=booking_id)

    # Fetch related objects (seats, movie, showtime, etc.)
    seats = booking.seats.all()  # All seats associated with this booking
    movie = booking.movie
    showtime = booking.showtime
    room = booking.room
    user = booking.user
    booking_time = booking.booking_time

    # Calculate total price for the seats
    total_price = sum(seat.price for seat in seats)

    # Render the template and pass the context
    context = {
        'booking': booking,
        'seats': seats,
        'movie': movie,
        'showtime': showtime,
        'room': room,
        'user': user,
        'booking_time': booking_time,
        'total_price': total_price
    }

    return render(request, 'bookings/booking_detail.html', context)

