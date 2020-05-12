from rest_framework import serializers
from api.integrator.models import Integrator


class IntegratorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Integrator
        fields = ('__all__')