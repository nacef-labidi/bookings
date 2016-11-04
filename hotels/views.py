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

	def get_context_data(self, **kwargs):
		context = super(HotelDetail, self).get_context_data(**kwargs)
		context['etoiles_range'] = range(self.object.etoiles)
		return context