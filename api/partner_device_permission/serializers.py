from rest_framework import serializers
from .models import PartnerDevicePermission


class PartnerDevicePermissionSerializer(serializers.ModelSerializer):


    class Meta:
        model = PartnerDevicePermission
        fields = ('__all__')