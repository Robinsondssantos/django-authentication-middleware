from django.db import models
from api.device.models import Device


class ReadingSmaai5(models.Model):
    description = models.CharField(max_length=50)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)