from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class StudentList(ListAPIView):
     # queryset=Student.objects.filter(passby='user1')
     queryset=Student.objects.all()
     serializer_class=StudentSerializers
     #check setting.py for global filter 
     filter_backends=[DjangoFilterBackend] #for per view setting
     # filterset_fields=['city']# write this in both i.e whether you are using global or per view setting
     filterset_fields=['name','city']# write this in both i.e whether you are using global or per view setting



     #when you want to show data that belongs to particular user
     # def get_queryset(self):
     #     user=self.request.user
     #     return Student.objects.filter(passby=user)




