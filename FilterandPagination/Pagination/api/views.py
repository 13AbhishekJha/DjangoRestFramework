from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import ListAPIView
from .mypagination import MyPagination
# Create your views here.

#Global pagination had been added in settings.py file


class StudentList(ListAPIView):
     queryset=Student.objects.all()
     serializer_class=StudentSerializers
     pagination_class=MyPagination #using Pagination PerView


 