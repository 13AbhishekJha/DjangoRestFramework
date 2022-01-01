from functools import partial
from django.urls import path,include
from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter

#creating router object
router=DefaultRouter()

#Register StudentViewSet with Router
# router.register('studentapi',views.StudentViewSet,basename='student')
router.register('studentapi',views.StudentModelViewSet
,basename='student')

router.register('student',views.StudentReadOnlyModelViewSet
,basename='student')

urlpatterns = [
    path('',include(router.urls))
]
