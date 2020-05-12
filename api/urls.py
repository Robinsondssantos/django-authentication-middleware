"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.integrator import views as integrator_views
from api.ownership import views as ownership_views
from api.nucleus import views as nucleus_views
from api.barn import views as barn_views
from api.device import views as device_views
from api.reading_smaai5 import views as reading_smaai5_views

router = routers.DefaultRouter()
router.register(r'api/v2/integrators', integrator_views.IntegratorViewSet)
router.register(r'api/v2/ownerships', ownership_views.OwnershipViewSet)
router.register(r'api/v2/nuclei', nucleus_views.NucleusViewSet)
router.register(r'api/v2/barns', barn_views.BarnViewSet)
router.register(r'api/v2/devices', device_views.DeviceViewSet)
router.register(r'api/v2/devices/device_id/readings', reading_smaai5_views.ReadingSmaai5ViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
