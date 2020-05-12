from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from api.ownership.models import Ownership
from api.ownership.serializers import OwnershipSerializer


class OwnershipViewSet(viewsets.ModelViewSet):
    queryset = Ownership.objects.all()
    serializer_class = OwnershipSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['description']
