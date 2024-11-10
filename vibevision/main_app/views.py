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

  return render(request, 'profile.html', context)
# Add new view
## ----------------------------------- Movie


## ----------------------------------- Room


## ----------------------------------- Showtime


## ----------------------------------- Seat


## ----------------------------------- BookingSeat


## ----------------------------------- Booking

