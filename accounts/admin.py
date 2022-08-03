from django.contrib import admin
# Register your models here.
from .models import *

#ignore this
# class RectifyAdmin(admin.ModelAdmin):
#     fields = ['store', 'report', 'status', 'issue', 'covid_compliance']

admin.site.register(Reportgeneration)
admin.site.register(approval_for_work)
admin.site.register(discrepancy_report)
admin.site.register(Maintable)
admin.site.register(Jobupdatestart)
admin.site.register(Jobupdateend)
admin.site.register(Jobupdatecomplete)