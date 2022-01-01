from functools import partial
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.

class StudentViewSet(viewsets.ViewSet):
      def list(self,request):
            print("*****List****")
            print("Basename:",self.basename)
            print("Action:",self.action)
            print("Detail:",self.detail)
            print("Suffix:",self.suffix)
            print("Name:",self.name)
            print("description:",self.description)
      
            stu=Student.objects.all()
            serializer=StudentSerializers(stu,many=True)
            return Response(serializer.data)

      def retrieve(self,request,pk= None):
            print("*****Retrieve****")
            print("Basename:",self.basename)
            print("Action:",self.action)
            print("Detail:",self.detail)
            print("Suffix:",self.suffix)
            print("Name:",self.name)
            print("description:",self.description)

            id=pk
            if id is not None:
             stu=Student.objects.get(id=id)
             serializer=StudentSerializers(stu)
             return Response(serializer.data)

      def create(self,request,format=None):
            print("*****List****")
            print("Basename:",self.basename)
            print("Action:",self.action)
            print("Detail:",self.detail)
            print("Suffix:",self.suffix)
            print("Name:",self.name)
            print("description:",self.description)
            serializer=StudentSerializers(data=request.data)
            if serializer.is_valid():
             serializer.save()
             return Response({"msg":"created successfully"},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.status.HTTP_400_BAD_REQUEST) 

      def update(self,request,pk= None,format=None):
            print("*****Update****")
            print("Basename:",self.basename)
            print("Action:",self.action)
            print("Detail:",self.detail)
            print("Suffix:",self.suffix)
            print("Name:",self.name)
            print("description:",self.description)

            id=pk
            stu=Student.objects.get(id=id)
            serializer=StudentSerializers(stu,data=request.data)
            if serializer.is_valid():
             serializer.save()
             return Response({"msg":"updated successfully"})
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

      def partial_update(self,request,pk= None,format=None):
            print("*****Partial_update(Patch)****")
            print("Basename:",self.basename)
            print("Action:",self.action)
            print("Detail:",self.detail)
            print("Suffix:",self.suffix)
            print("Name:",self.name)
            print("description:",self.description)
            id=pk
            stu=Student.objects.get(id=id)
            serializer=StudentSerializers(stu,data=request.data,partial=True)
            if serializer.is_valid():
             serializer.save()
             return Response({"msg":"updated successfully"})
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
      
      def destroy(self,request,pk= None,format=None):
            print("*****delete****")
            print("Basename:",self.basename)
            print("Action:",self.action)
            print("Detail:",self.detail)
            print("Suffix:",self.suffix)
            print("Name:",self.name)
            print("description:",self.description)
            id=pk
            stu=Student.objects.get(id=id)
            stu.delete()
            return Response({"msg":"Deleted successfully"})  
