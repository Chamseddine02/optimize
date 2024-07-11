# apps/store/models/article.py

from django.db import models


class Article(models.Model):
    ref = models.CharField(max_length=255, unique=True)
    libelle = models.CharField(max_length=255)
    gamme = models.ForeignKey("Gamme", to_field="id", on_delete=models.CASCADE)
    statut_article = models.CharField(max_length=255, default="Soldeur")
    adresse_vidage = models.CharField(max_length=255, default="F00000")
    poids = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.libelle
