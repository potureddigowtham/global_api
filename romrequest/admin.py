from django.contrib import admin
from .models import WebApp
from import_export.admin import ImportExportModelAdmin


@admin.register(WebApp)
class ViewAdmin(ImportExportModelAdmin):
    pass