from django.shortcuts import render
from .models import WebApp
from .serializers import WebAppSerializer
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes

class WebAppViewset(viewsets.ModelViewSet):
    queryset = WebApp.objects.all()
    serializer_class = WebAppSerializer

    