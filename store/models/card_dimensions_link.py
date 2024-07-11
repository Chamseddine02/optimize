# apps/store/models/card_dimensions_link.py
from django.db import models
from .carton import Carton
from .dimension import Dimension


class CardDimensionsLink(models.Model):
    carton = models.ForeignKey(Carton, on_delete=models.CASCADE)
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)
    percent_value = models.FloatField()

    def __str__(self):
        return f"Link between {self.carton} and {self.dimension}"
