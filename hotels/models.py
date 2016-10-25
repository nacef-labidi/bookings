from __future__ import unicode_literals

from django.db import models


class Hotel(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    etoiles = models.PositiveSmallIntegerField()
    chambres = models.PositiveIntegerField()
    clients = models.ManyToManyField('Client', through='Reservation')

    def __str__(self):
        return self.nom


class Client(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_reservation = models.DateField()