from django.urls import path
from . import views

urlpatterns = [
    path("student",views.get_Student),
    path("student/<int:id>",views.get_Student_by_ID)
]
