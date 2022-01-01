from django.urls import path
from . import views

urlpatterns = [
    path("student",views.StudentListCreate.as_view()),
    path("student/<int:pk>",views.StudentRetrieveUpdateDestroyAPIView.as_view())
]
