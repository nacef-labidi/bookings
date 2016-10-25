from __future__ import unicode_literals

from django.db import models

class Vol(models.Model):
    numero = models.CharField(max_length=10)
    depart = models.DateTimeField()
    arrivee = models.DateTimeField()
    origine =  models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    modele = models.CharField(max_length=10)

    def __str__(self):
        return self.numero
