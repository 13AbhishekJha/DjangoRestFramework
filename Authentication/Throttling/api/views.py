from .models import Student
from .serializers import StudentSerializers
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
# Create your views here.
#do all these from admin panel user section
#user-you need to create and check active
#Admin-you need to create and check active and staff_status
#superadmin-all permission

#using ModelViewSet
class StudentModelViewSet(viewsets.ModelViewSet):
      queryset=Student.objects.all()
      serializer_class=StudentSerializers
      authentication_classes=[SessionAuthentication]
      permission_classes=[IsAuthenticatedOrReadOnly]
      throttle_classes=[AnonRateThrottle,UserRateThrottle]

      


      
