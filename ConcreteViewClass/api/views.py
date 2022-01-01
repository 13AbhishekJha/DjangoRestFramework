from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.

class StudentListCreate(ListCreateAPIView):
     queryset=Student.objects.all()
     serializer_class=StudentSerializers 

class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
     queryset=Student.objects.all()
     serializer_class=StudentSerializers  


#single use

# class StudentList(ListAPIView):
#      queryset=Student.objects.all()
#      serializer_class=StudentSerializers

# class StudentCreate(CreateAPIView):
#      queryset=Student.objects.all()
#      serializer_class=StudentSerializers

# class StudentRetrieve(RetrieveAPIView):
#      queryset=Student.objects.all()
#      serializer_class=StudentSerializers

# class StudentUpdate(UpdateAPIView):
#      queryset=Student.objects.all()
#      serializer_class=StudentSerializers

# class StudentDelete(DestroyAPIView):
#      queryset=Student.objects.all()
#      serializer_class=StudentSerializers     

# class StudentListCreate(ListCreateAPIView):
#      queryset=Student.objects.all()
#      serializer_class=StudentSerializers 

# class StudentRetrieveUpdate(RetrieveUpdateAPIView):
#      queryset=Student.objects.all()
#      serializer_class=StudentSerializers 


# class StudentRetrieveDestroy(RetrieveDestroyAPIView):
#      queryset=Student.objects.all()
#      serializer_class=StudentSerializers      

     

 #grouped
# class student_get_and_create(GenericAPIView,ListModelMixin,CreateModelMixin):
#        queryset=Student.objects.all()
#        serializer_class=StudentSerializers

#        def get(self,request,*args,**kwargs):
#             return self.list(request,*args,**kwargs)

#        def post(self,request,*args,**kwargs):
#              return self.create(request,*args,**kwargs)


# class student_get_update_delete_by_id(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
#        queryset=Student.objects.all()
#        serializer_class=StudentSerializers

#        def get(self,request,*args,**kwargs):
#             return self.retrieve(request,*args,**kwargs)

#        def put(self,request,*args,**kwargs):
#             return self.update(request,*args,**kwargs)

#        def delete(self,request,*args,**kwargs):
#             return self.destroy(request,*args,**kwargs)   


