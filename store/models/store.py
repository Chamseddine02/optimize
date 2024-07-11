# apps/store/models/store.py
from django.db import models


class Store(models.Model):
    store_name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    occupancy_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.store_name
