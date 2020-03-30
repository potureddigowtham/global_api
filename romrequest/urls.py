from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RomRequestViewset, Emp

router = DefaultRouter()
router.register(r'romrequest', RomRequestViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('empstats', Emp),
]