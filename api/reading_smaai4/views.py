from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.response import Response
from rest_framework.views import APIView
from api.reading_smaai4.models import ReadingSmaai4
from api.reading_smaai4.serializers import ReadingSmaai4Serializer


class ReadingSmaai4View(APIView):

  # @method_decorator(cache_page(60*60*2))
  def get(self, request):
      fruit = cache.get('fruit')
      if fruit:
          print('my cache:', fruit)
      cache.set('fruit', 'apple')
      reading = ReadingSmaai4.objects.all()
      serializer = ReadingSmaai4Serializer(reading, many=True)
      return Response(serializer.data)

  def post(self, request):
      record = request.data.get('reading')

      serializer = ReadingSmaai4Serializer(data=record)
      if serializer.is_valid(raise_exception=True):
          record_saved = serializer.save()
      return Response(record_saved)
