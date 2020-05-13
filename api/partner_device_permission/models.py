from django.db import models
from django.contrib.auth.models import User
from api.device.models import Device


class PartnerDevicePermission(models.Model):
    partner = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
