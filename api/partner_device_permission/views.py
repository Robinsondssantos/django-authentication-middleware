from django.core.cache import cache
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .models import PartnerDevicePermission
from .serializers import PartnerDevicePermissionSerializer


class PartnerDevicePermissionViewSet(viewsets.ModelViewSet):
    queryset = PartnerDevicePermission.objects.all()
    serializer_class = PartnerDevicePermissionSerializer
    permission_class = (DjangoModelPermissions,)

    def list(self, request, *args, **kwargs):
        cached = cache.get('PartnerDevicePermission_UserId_{}'.format(request.user.id))
        print('cache:', cached)
        if not cached:
            print('não tem nada cacheado')
            queryset = self.filter_queryset(self.get_queryset())

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            print('serializer:', serializer)

            cache.set('PartnerDevicePermission_UserId_{}'.format(request.user.id), serializer.data)

        return Response(cached if cached else serializer.data)    
