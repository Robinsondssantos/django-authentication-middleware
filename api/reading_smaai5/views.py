from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from .models import ReadingSmaai5
from .serializers import ReadingSmaai5Serializer


class ReadingSmaai5ViewSet(viewsets.ModelViewSet):
    queryset = ReadingSmaai5.objects.all()
    serializer_class = ReadingSmaai5Serializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['description']



