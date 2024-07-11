# apps/store/models/stage.py
from django.db import models


class Stage(models.Model):
    stage_number = models.IntegerField()

    def __str__(self):
        return f"Stage {self.stage_number}"
