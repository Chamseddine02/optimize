# apps/store/models/user.py

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.title
