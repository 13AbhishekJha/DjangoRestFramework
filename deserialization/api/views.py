from django.shortcuts import render
from rest_framework import serializers
from .models import Student
from .serializers import StudentSerializers
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializers(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={"msg":"created successfully"}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type="application/json")
        
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type="application/json")
        