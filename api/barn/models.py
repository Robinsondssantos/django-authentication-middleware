from django.db import models
from api.nucleus.models import Nucleus


class Barn(models.Model):
    description = models.CharField(max_length=50)
    nucleus = models.ForeignKey(Nucleus, on_delete=models.CASCADE)

