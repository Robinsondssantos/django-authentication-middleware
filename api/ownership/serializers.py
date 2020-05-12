from rest_framework import serializers
from api.ownership.models import Ownership


class OwnershipSerializer(serializers.ModelSerializer):


    class Meta:
        model = Ownership
        fields = ('__all__')