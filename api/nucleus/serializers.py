from rest_framework import serializers
from api.nucleus.models import Nucleus


class NucleusSerializer(serializers.ModelSerializer):


  class Meta:
      model = Nucleus
      fields = ('__all__')