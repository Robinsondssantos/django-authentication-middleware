from django.db import models


class Integrator(models.Model):
    description = models.CharField(max_length=50)
