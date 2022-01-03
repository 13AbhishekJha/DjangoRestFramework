from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
# Create your views here.

# class StudentList(ListAPIView):
#      # queryset=Student.objects.filter(passby='user1')
#      queryset=Student.objects.all()
#      serializer_class=StudentSerializers
#      #check setting.py for global filter 
#      filter_backends=[DjangoFilterBackend] #for per view setting
#      # filterset_fields=['^city']# write this in both i.e whether you are using global or per view setting
#      # filterset_fields=['name','city']# write this in both i.e whether you are using global or per view setting

     #when you want to show data that belongs to particular user
     # def get_queryset(self):
     #     user=self.request.user
     #     return Student.objects.filter(passby=user)



#using search filter


# class StudentList(ListAPIView):
#      queryset=Student.objects.all()
#      serializer_class=StudentSerializers
#      filter_backends=[SearchFilter] 
#      search_fields=['city']# http://127.0.0.1:8000/student/?search=Noida
#      search_fields=['^name']#start with

#if you want to override search= type written then in settings.py
# REST_FRAMEWORK={
#      'SEARCH_PARAM':'name'
# }


#ordering filter

class StudentList(ListAPIView):
     queryset=Student.objects.all()
     serializer_class=StudentSerializers
     filter_backends=[OrderingFilter] 
     # ordering_fields=['city']# http://127.0.0.1:8000/student/?ordering=city
