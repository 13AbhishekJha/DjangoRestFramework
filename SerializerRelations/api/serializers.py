from django.db import models
from rest_framework import serializers, validators
from .models import Singer,Song


class SongSerializers(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields=['id','title','singer','duration']


class SingerSerializers(serializers.ModelSerializer):
    # song=serializers.StringRelatedField(many=True,read_only=True)
    # song=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name="song-detail")
    song=serializers.SlugRelatedField(many=True,read_only=True,slug_field="title")

    class Meta:
        model=Singer
        fields=['id','name','gender','song']        