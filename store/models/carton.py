# apps/store/models/carton.py

from django.db import models


class Carton(models.Model):
    refCarton = models.CharField(max_length=255, unique=True)
    libelle = models.CharField(max_length=255)
    height_cart = models.FloatField()
    length_cart = models.FloatField()
    breadth_cart = models.FloatField()

    def __str__(self):
        return self.libelle
