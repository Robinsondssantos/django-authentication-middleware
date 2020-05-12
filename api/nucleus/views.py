from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from api.nucleus.models import Nucleus
from api.nucleus.serializers import NucleusSerializer


class NucleusViewSet(viewsets.ModelViewSet):
    queryset = Nucleus.objects.all()
    serializer_class = NucleusSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['description']



