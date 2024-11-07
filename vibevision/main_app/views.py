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


## ----------------------------------- Room


## ----------------------------------- Showtime


## ----------------------------------- Seat


## ----------------------------------- BookingSeat


## ----------------------------------- Booking

