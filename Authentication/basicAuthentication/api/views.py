from rest_framework import authentication
from .models import Student
from .serializers import StudentSerializers
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here
#do all these from admin panel user section
#user-you need to create and check active
#Admin-you need to create and check active and staff_status
#superadmin-all permission.

#using ModelViewSet
class StudentModelViewSet(viewsets.ModelViewSet):
      queryset=Student.objects.all()
      serializer_class=StudentSerializers
      # permission_classes=[IsAdminUser] # check staff_status to reach out to api
#for globally defining Authentication(i.e when you have more than one viewset and you want to set on all) see settings.py
      # authentication_classes=[BasicAuthentication]
      # permission_classes=[IsAuthenticated]
      

#If you want to override default behaviour 

# class StudentModelViewSetDummy(viewsets.ModelViewSet):
#       queryset=Student.objects.all()
#       serializer_class=StudentSerializers
#       # authentication_classes=[BasicAuthentication]
#       # permission_classes=[AllowAny]

