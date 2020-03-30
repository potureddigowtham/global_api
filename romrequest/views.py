from django.shortcuts import render
from .models import RomRequest, Employees, CEmployees
from .serializers import RomRequestSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes


class RomRequestViewset(viewsets.ModelViewSet):
    queryset = RomRequest.objects.all()
    serializer_class = RomRequestSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        try:
            user = self.request.user.username
            print(user)
            data = Employees.objects.filter(emp_domain_id=user.upper())
            
            for i in data:
                user_email_id = i.email_id
                user_manager_id = i.mgr_domain_id

            manager_data = Employees.objects.filter(emp_domain_id=user_manager_id.upper())
            print(manager_data)
            for i in manager_data:
                manager_1_email_id = i.email_id
                manager_id_2 = i.mgr_domain_id

            serializer.save(requested_by = user, 
            requested_user_email = user_email_id,
            manager_id_1 = user_manager_id,
            manager_id_1_email = manager_1_email_id,
            manager_id_2 = manager_id_2,
            manager_id_2_email = "changed@sample.com")
        except:
            serializer.save(requested_by = user,
            manager_id_2 = "None",
            manager_id_2_email = "changed@sample.com")
        

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def Emp(request, format=None):
    FTE = Employees.objects.filter(emp_type="FTE").count()
    GET = Employees.objects.filter(emp_type="GET").count()
    PGET = Employees.objects.filter(emp_type="PGET").count()
    CE = CEmployees.objects.all().count()
    context = {
        'FTE': FTE,
        'GET': GET,
        'PGET': PGET,
        'CE': CE,
    }
    return Response(context)

    