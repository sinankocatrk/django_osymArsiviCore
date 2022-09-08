from django.contrib import admin

from kontenjan.models import Ebe,Hemsire
from import_export.admin import ImportExportModelAdmin

@admin.register(Ebe,Hemsire)

class VievAdmin(ImportExportModelAdmin):
    
    pass

