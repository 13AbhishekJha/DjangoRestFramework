from rest_framework.response import Response
from .models import Song,Singer
from .serializers import SongSerializers,SingerSerializers
from rest_framework import viewsets
# Create your views here.

class SingerViewset(viewsets.ModelViewSet):
      queryset=Singer.objects.all()
      serializer_class=SingerSerializers


class SongViewset(viewsets.ModelViewSet):
      queryset=Song.objects.all()
      serializer_class=SongSerializers