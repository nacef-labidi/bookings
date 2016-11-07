from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Hotel

# @login_required()
# def index(request):
# 	return render(request, 'index.html', {})

class HotelList(ListView):
	model = Hotel

class HotelCreate(CreateView):
	model = Hotel
	fields = ['nom', 'description', 'etoiles', 'chambres']
	success_url = '/'

class HotelDetail(DetailView):
	model = Hotel

	def get_context_data(self, **kwargs):
		context = super(HotelDetail, self).get_context_data(**kwargs)
		context['etoiles_range'] = range(self.object.etoiles)
		return context