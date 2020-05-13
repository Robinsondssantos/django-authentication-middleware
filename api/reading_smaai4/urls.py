from django.urls import path
from .views import ReadingSmaai4View


app_name = 'reading_smaai4'


urlpatterns = [
    path('reading_smaai4', ReadingSmaai4View.as_view())
]
