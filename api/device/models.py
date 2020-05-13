from django.db import models
from api.barn.models import Barn


class Device(models.Model):
    description = models.CharField(max_length=50)
    barn = models.ForeignKey(Barn, on_delete=models.CASCADE)

    def __str__(self):
        return self.description




