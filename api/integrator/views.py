from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from api.integrator.models import Integrator
from api.integrator.serializers import IntegratorSerializer


class IntegratorViewSet(viewsets.ModelViewSet):
    queryset = Integrator.objects.all()
    serializer_class = IntegratorSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['description']
