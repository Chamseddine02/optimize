# apps/store/models/calibrage.py

from django.db import models
from .article import Article
from .carton import Carton


class Calibration(models.Model):
    ref_article = models.ForeignKey(Article, to_field="ref", on_delete=models.CASCADE)
    carton = models.ForeignKey(Carton, to_field="id", on_delete=models.CASCADE)
    commentaire = models.CharField(max_length=60000)
    quantite = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ref_article} - {self.carton}"
