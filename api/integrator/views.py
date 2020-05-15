from rest_framework import viewsets
from rest_framework import filters
# from rest_framework.permissions import DjangoModelPermissions
from api.permissions.permissions import CustomDjangoModelPermissions
from api.integrator.models import Integrator
from api.integrator.serializers import IntegratorSerializer


class IntegratorViewSet(viewsets.ModelViewSet):
    queryset = Integrator.objects.all()
    serializer_class = IntegratorSerializer
    permission_classes = (CustomDjangoModelPermissions,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['description']

# from rest_framework import generics
# from rest_framework.permissions import DjangoModelPermissions
# from api.integrator.models import Integrator
# from api.integrator.serializers import IntegratorSerializer


# class IntegratorViewSet(generics.ListCreateAPIView, 
#                         generics.RetrieveUpdateDestroyAPIView):

#     # queryset = Integrator.objects.all()
#     serializer_class = IntegratorSerializer
#     permission_classes = (DjangoModelPermissions,)

#     def get_queryset(self):
#         return Integrator.objects.all()



