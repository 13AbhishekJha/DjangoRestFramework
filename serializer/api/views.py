from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializers
from django.http import HttpResponse
# Create your views here.

def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    # print("stu data")
    # print(stu)
    serializer=StudentSerializers(stu)
    # print("serializer data")
    # print(serializer)
    json_data=JSONRenderer().render(serializer.data)
    # print("serialer.data ")
    # print(serializer.data)
    # print("json data")
    # print(json_data)
    return HttpResponse(json_data,content_type="application/json")
    # return JsonResponse(serializer.data)

def student_detail_all(request):
    stu=Student.objects.all()
    serializer=StudentSerializers(stu,many=True)
    # print("serialer.data ")
    # print(serializer.data)
    # json_data=JSONRenderer().render(serializer.data)
    # print("json data")
    # print(json_data)
    # return HttpResponse(json_data,content_type="application/json")
    return JsonResponse(serializer.data,safe=False)   
