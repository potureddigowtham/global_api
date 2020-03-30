from django.contrib import admin
from .models import RomRequest, Employees, CEmployees
from import_export.admin import ImportExportModelAdmin


@admin.register(RomRequest,Employees,CEmployees)
class ViewAdmin(ImportExportModelAdmin):
    pass