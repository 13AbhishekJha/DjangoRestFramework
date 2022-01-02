from rest_framework import authentication
from .models import Student
from .serializers import StudentSerializers
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

# Create your views here.
#do all these from admin panel user section
#user-you need to create and check active
#Admin-you need to create and check active and staff_status
#superadmin-all permission

#using ModelViewSet
class StudentModelViewSet(viewsets.ModelViewSet):
      queryset=Student.objects.all()
      serializer_class=StudentSerializers
      authentication_classes=[TokenAuthentication]
      permission_classes=[IsAuthenticated]#You can any Permission class

      


      
