from django.urls import path
from . import views

urlpatterns = [
    path("student",views.student_api),
    path("student/<int:id>",views.student_api_by_ID)
]
