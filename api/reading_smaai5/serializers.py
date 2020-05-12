from rest_framework import serializers
from api.reading_smaai5.models import ReadingSmaai5


class ReadingSmaai5Serializer(serializers.ModelSerializer):


  class Meta:
      model = ReadingSmaai5
      fields = ('__all__')