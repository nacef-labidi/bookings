from django.shortcuts import render

from .models import Hotel

def index(request):
    hotels = Hotel.objects.all()
    return render(request, 'index.html', {'hotels': hotels})
