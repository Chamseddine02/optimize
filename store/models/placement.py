# apps/store/models/placement.py
from django.db import models
from .article import Article
from .locker import Locker
from .user import User


class Placement(models.Model):
    article = models.ForeignKey(Article, to_field="id", on_delete=models.CASCADE)
    locker = models.ForeignKey(Locker, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    capacity = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Placement {self.id}"
