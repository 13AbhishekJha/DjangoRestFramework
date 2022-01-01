from functools import partial
from django.urls import path,include
from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter

#creating router object
router=DefaultRouter()

#Register StudentViewSet with Router
router.register('studentapi',views.StudentViewSet,basename='student')

urlpatterns = [
    # path("student",views.StudentAPI.as_view()),
    # path("student/<int:pk>",views.StudentAPI.as_view())
    path('',include(router.urls))
]
