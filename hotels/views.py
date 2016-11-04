from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Hotel

class HotelList(ListView):
	model = Hotel

class HotelCreate(CreateView):
	model = Hotel
	fields = ['nom', 'description', 'etoiles', 'chambres']
	success_url = '/hotels'

class HotelDetail(DetailView):
	model = Hotel