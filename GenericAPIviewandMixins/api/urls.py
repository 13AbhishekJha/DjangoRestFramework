from django.urls import path
from . import views

urlpatterns = [
    path("student",views.student_get_and_create.as_view()),
    path("student/<int:pk>",views.student_get_update_delete_by_id.as_view())
]
