from rest_framework import serializers
from api.reading_smaai4.models import ReadingSmaai4
from api.device.serializers import DeviceSerializer


# class ReadingSmaai4Serializer(serializers.ModelSerializer):


#   class Meta:
#       model = ReadingSmaai4
#       fields = ('__all__')

class ReadingSmaai4Serializer(serializers.Serializer):
    id = serializers.IntegerField()
    description = serializers.CharField(max_length=50)
    # device = DeviceSerializer()
    device_id = serializers.IntegerField()

    def create(self, validated_data):
        return super().create(validated_data)

