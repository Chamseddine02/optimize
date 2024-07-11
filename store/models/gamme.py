# apps/store/models/gamme.py
from django.db import models


class Gamme(models.Model):
    name = models.CharField(max_length=255)  # Example field

    def __str__(self):
        return self.name
