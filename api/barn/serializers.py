from rest_framework import serializers
from api.barn.models import Barn


class BarnSerializer(serializers.ModelSerializer):


  class Meta:
      model = Barn
      fields = ('__all__')