from functools import partial
from django.urls import path,include
from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
#creating router object
router=DefaultRouter()

router.register('studentapi',views.StudentModelViewSet
,basename='student')

urlpatterns = [
    path('',include(router.urls)),#for ViewSet
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),#for browser API
    path('gettoken/',obtain_auth_token)#for Token Auth
]
