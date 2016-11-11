from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ContactForm

from .models import Hotel, Reservation

# @login_required()
# def index(request):
# 	return render(request, 'index.html', {})
#
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

class ContactView(LoginRequiredMixin, FormView):
	form_class = ContactForm
	template_name = 'contact.html'


class ReservationCreate(CreateView):
	model = Reservation
	fields = ['hotel', 'date_reservation']
	success_url = '/'

	def form_valid(self, form):
		form.instance.client = self.request.user.client
		return super(ReservationCreate, self).form_valid(form)

	def get_initial(self):
		initial = super(ReservationCreate, self).get_initial()
		initial['hotel'] = self.kwargs['hotel_id']
		return initial