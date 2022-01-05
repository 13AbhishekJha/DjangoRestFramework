from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from . import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('singer',views.SingerViewset,basename='singer')
router.register('song',views.SongViewset,basename='song')

urlpatterns = [
    path('',include(router.urls))
]
