from django.db import models
from api.ownership.models import Ownership


class Nucleus(models.Model):
    description = models.CharField(max_length=50)
    ownership = models.ForeignKey(Ownership, on_delete=models.CASCADE)