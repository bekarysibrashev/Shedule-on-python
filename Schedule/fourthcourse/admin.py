from django.contrib import admin
from unicodedata import category
from .models import Schedule4

from import_export.admin import ImportExportActionModelAdmin as ieama
from import_export import resources
from import_export import fields 
from import_export.widgets import ForeignKeyWidget


class ScheduleRecource(resources.ModelResource):    
   

    class Meta:
        model = Schedule4
       

class ScheduleAdmin(ieama):
    resource_class = ScheduleRecource
    # list_display = [field.day for field in Schedule._meta.fields if field.day !='day']
    # import_id_fields = ['day']

admin.site.register(Schedule4, ScheduleAdmin)

# Register your models here.
