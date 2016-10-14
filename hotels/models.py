from __future__ import unicode_literals

from django.db import models

class Hotel(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    etoiles = models.PositiveSmallIntegerField()
    chambres = models.PositiveIntegerField()

    def __str__(self):
        return self.nom
