from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WebAppViewset

router = DefaultRouter()
router.register(r'webapp', WebAppViewset)

urlpatterns = [
    path('', include(router.urls)),
]