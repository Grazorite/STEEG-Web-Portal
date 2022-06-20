from django.contrib import admin
# Register your models here.
from .models import *

#ignore this
# class RectifyAdmin(admin.ModelAdmin):
#     fields = ['store', 'report', 'status', 'issue', 'covid_compliance']

admin.site.register(steeg_user)
admin.site.register(job_status)
admin.site.register(equipment_inventory)
admin.site.register(approval_for_work)
admin.site.register(discrepancy_report)
admin.site.register(Ip220610Cleaned)
admin.site.register(JobUpdateStart)
admin.site.register(JobUpdateEnd)
admin.site.register(JobUpdateComplete)