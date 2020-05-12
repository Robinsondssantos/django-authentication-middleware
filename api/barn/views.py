from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from api.barn.models import Barn
from api.barn.serializers import BarnSerializer


class BarnViewSet(viewsets.ModelViewSet):
    queryset = Barn.objects.all()
    serializer_class = BarnSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['description']