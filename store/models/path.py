# apps/store/models/path.py
from django.db import models


class Path(models.Model):
    path_number = models.IntegerField()
    length = models.IntegerField()

    def __str__(self):
        return f"Path {self.path_number}"
