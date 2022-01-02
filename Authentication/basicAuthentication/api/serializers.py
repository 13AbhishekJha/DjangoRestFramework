from django.db import models
from rest_framework import serializers, validators
from .models import Student


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','roll','city']