from django.shortcuts import render

from .models import Vol


def index(request):
    vols = Vol.objects.all()
    return render(request, 'vols.html', {'vols':vols})
