# apps/store/models/dimension.py
from django.db import models


class Dimension(models.Model):
    height = models.IntegerField()
    breadth = models.IntegerField()
    length = models.IntegerField()

    def __str__(self):
        return f"Dimension {self.id}"
