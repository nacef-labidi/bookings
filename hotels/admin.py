from django.contrib import admin

from .models import Hotel, Client, Reservation

admin.site.register(Hotel)
admin.site.register(Client)
admin.site.register(Reservation)