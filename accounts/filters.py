import django_filters
from django_filters import DateRangeFilter, DateFilter, DateFromToRangeFilter
from django_filters.widgets import RangeWidget
from .models import *

######################FILTER FOR APPROVALS PAGE##########################
class ApprovalFilter(django_filters.FilterSet):
    class Meta:
        model = Maintable
        fields = {
            'approval_status': ['exact'],
            'service_order': ['icontains']
            }

#####################FILTER FOR JOBS PAGE################################
class JobFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='mal_start',lookup_expr=('gt'),) 
    end_date = DateFilter(field_name='mal_start',lookup_expr=('lt'))
    # date_range1 = DateFromToRangeFilter(widget=RangeWidget(attrs={'type':'date'}))
    date_range = DateRangeFilter(field_name='mal_start')
    class Meta:
        model = Reportgeneration
        fields = {
            'service_order': ['icontains'],
            'priority_text': ['exact'],
            }

# class DateFilter(django_filters.DateRangeFilter): 
#     class Meta:
#         model =  Reportgeneration
#         fields = ['mal_start']
