# apps/store/models/locker.py

from django.db import models


class Locker(models.Model):
    dimension = models.ForeignKey("Dimension", to_field="id", on_delete=models.CASCADE)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
