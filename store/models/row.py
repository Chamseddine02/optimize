# apps/store/models/row.py
from django.db import models


class Row(models.Model):
    row_number = models.IntegerField()

    def __str__(self):
        return f"Row {self.row_number}"
