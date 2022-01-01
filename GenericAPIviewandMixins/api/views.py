from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# Create your views here.

#grouped
class student_get_and_create(GenericAPIView,ListModelMixin,CreateModelMixin):
       queryset=Student.objects.all()
       serializer_class=StudentSerializers

       def get(self,request,*args,**kwargs):
            return self.list(request,*args,**kwargs)

       def post(self,request,*args,**kwargs):
             return self.create(request,*args,**kwargs)


class student_get_update_delete_by_id(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
       queryset=Student.objects.all()
       serializer_class=StudentSerializers

       def get(self,request,*args,**kwargs):
            return self.retrieve(request,*args,**kwargs)

       def put(self,request,*args,**kwargs):
            return self.update(request,*args,**kwargs)

       def delete(self,request,*args,**kwargs):
            return self.destroy(request,*args,**kwargs)   




# class StudentList(GenericAPIView,ListModelMixin):
#       queryset=Student.objects.all()
#       serializer_class=StudentSerializers

#       def get(self,request,*args,**kwargs):
#             return self.list(request,*args,**kwargs)

# class StudentCreate(GenericAPIView,CreateModelMixin):
#       queryset=Student.objects.all()
#       serializer_class=StudentSerializers

#       def post(self,request,*args,**kwargs):
#             return self.create(request,*args,**kwargs)

# class StudentRetrieve(GenericAPIView,RetrieveModelMixin):
#       queryset=Student.objects.all()
#       serializer_class=StudentSerializers

#       def get(self,request,*args,**kwargs):
#             return self.retrieve(request,*args,**kwargs)

# class StudentUpdate(GenericAPIView,UpdateModelMixin):
#       queryset=Student.objects.all()
#       serializer_class=StudentSerializers

#       def put(self,request,*args,**kwargs):
#             return self.update(request,*args,**kwargs)

# class StudentDelete(GenericAPIView,DestroyModelMixin):
#       queryset=Student.objects.all()
#       serializer_class=StudentSerializers

#       def delete(self,request,*args,**kwargs):
#             return self.destroy(request,*args,**kwargs)







# class StudentAPI(APIView):
#       def get(self,request,pk= None,format=None):
#             id=pk
#             if id is not None:
#              stu=Student.objects.get(id=id)
#              serializer=StudentSerializers(stu)
#              return Response(serializer.data)

#             stu=Student.objects.all()
#             serializer=StudentSerializers(stu,many=True)
#             return Response(serializer.data)

#       def post(self,request,format=None):
#         serializer=StudentSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg":"created successfully"},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.status.HTTP_400_BAD_REQUEST) 

#       def patch(self,request,pk= None,format=None):
#             id=pk
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializers(stu,data=request.data,partial=True)
#             if serializer.is_valid():
#              serializer.save()
#              return Response({"msg":"updated successfully"})
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

#       def put(self,request,pk= None,format=None):
#             id=pk
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializers(stu,data=request.data)
#             if serializer.is_valid():
#              serializer.save()
#              return Response({"msg":"updated successfully"})
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
      
#       def delete(self,request,pk= None,format=None):
#             id=pk
#             stu=Student.objects.get(id=id)
#             stu.delete()
#             return Response({"msg":"Deleted successfully"})  