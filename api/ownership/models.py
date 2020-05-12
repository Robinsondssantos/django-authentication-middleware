from django.db import models
from api.integrator.models import Integrator


class Ownership(models.Model):
    description = models.CharField(max_length=50)    
    integrator = models.ForeignKey(Integrator, on_delete=models.CASCADE)
