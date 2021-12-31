from functools import partial
from django.shortcuts import render
from .models import Student
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializers
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def get_Student_by_ID(request,id):
   if request.method=='GET':
     stu=Student.objects.get(id=id)
     serializer=StudentSerializers(stu)
    #  json_data=JSONRenderer().render(serializer.data)
    #  return HttpResponse(json_data,content_type="application/json")
     return JsonResponse(serializer.data)

   if request.method=='PUT': 
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        stu=Student.objects.get(id=id)
        serializer=StudentSerializers(stu,data=pythondata,partial=True)  #for full update remove partial=True 
        if serializer.is_valid():
            serializer.save()
            res={"msg":"Updated successfully"}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type="application/json")
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type="application/json") 

   if request.method=='DELETE':
     stu=Student.objects.get(id=id)
     stu.delete()
     res={"msg":"Deleted successfully"}
    #  json_data=JSONRenderer().render(res)
    #  return HttpResponse(json_data,content_type="application/json")  
     return JsonResponse(res,safe=False) 



@csrf_exempt    
def get_Student(request):
    
   if request.method=='GET':
    stu=Student.objects.all()
    serializer=StudentSerializers(stu,many=True)
    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type="application/json")
    return JsonResponse(serializer.data,safe=False) 

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
  
