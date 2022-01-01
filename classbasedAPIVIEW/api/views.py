from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class StudentAPI(APIView):
      def get(self,request,pk= None,format=None):
            id=pk
            if id is not None:
             stu=Student.objects.get(id=id)
             serializer=StudentSerializers(stu)
             return Response(serializer.data)

            stu=Student.objects.all()
            serializer=StudentSerializers(stu,many=True)
            return Response(serializer.data)

      def post(self,request,format=None):
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"created successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.status.HTTP_400_BAD_REQUEST) 

      def patch(self,request,pk= None,format=None):
            id=pk
            stu=Student.objects.get(id=id)
            serializer=StudentSerializers(stu,data=request.data,partial=True)
            if serializer.is_valid():
             serializer.save()
             return Response({"msg":"updated successfully"})
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

      def put(self,request,pk= None,format=None):
            id=pk
            stu=Student.objects.get(id=id)
            serializer=StudentSerializers(stu,data=request.data)
            if serializer.is_valid():
             serializer.save()
             return Response({"msg":"updated successfully"})
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
      
      def delete(self,request,pk= None,format=None):
            id=pk
            stu=Student.objects.get(id=id)
            stu.delete()
            return Response({"msg":"Deleted successfully"})  





# @api_view(['GET','POST','PUT','DELETE']) 
# def student_api(request,pk=None):
#       if request.method=='GET':
#             id=pk
#             if id is not None:
#              stu=Student.objects.get(id=id)
#              serializer=StudentSerializers(stu)
#              return Response(serializer.data)

#             stu=Student.objects.all()
#             serializer=StudentSerializers(stu,many=True)
#             return Response(serializer.data)

#       if request.method=='POST':
#         serializer=StudentSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg":"created successfully"},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.status.HTTP_400_BAD_REQUEST) 

#       if request.method=='PUT':
#             id=pk
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializers(stu,data=request.data,partial=True)
#             if serializer.is_valid():
#              serializer.save()
#              return Response({"msg":"updated successfully"})
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

#       if request.method=='DELETE':
#             id=pk
#             stu=Student.objects.get(id=id)
#             stu.delete()
#             return Response({"msg":"Deleted successfully"})                





# @api_view(['GET','POST'])
# def student_api(request):
#     if request.method=='GET':
#         stu=Student.objects.all()
#         serializer=StudentSerializers(stu,many=True)
#         return Response(serializer.data)    
#     if request.method=='POST':
#         serializer=StudentSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg":"created successfully"})
#         return Response(serializer.errors)  


# @api_view(['GET','PUT','DELETE'])
# def student_api_by_ID(request,id):
#     if request.method=='GET':
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializers(stu)
#             return Response(serializer.data)

#     if request.method=='PUT':
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializers(stu,data=request.data,partial=True)
#             if serializer.is_valid():
#              serializer.save()
#              return Response({"msg":"updated successfully"})
#             return Response(serializer.errors) 

#     if request.method=='DELETE':
#             stu=Student.objects.get(id=id)
#             stu.delete()
#             return Response({"msg":"Deleted successfully"})
            

