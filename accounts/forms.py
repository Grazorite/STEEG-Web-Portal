from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Order, Ip220610Cleaned, JobUpdateStart, JobUpdateEnd, JobUpdateComplete, steeg_user, job_status, equipment_inventory, approval_for_work, discrepancy_report
from .widgets import DatePickerInput, DateTimePickerInput

class RectifyForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['store', 'Non_FB_Report', 'FB_Report',
                  'Covid_Compliance_Report', 'upload_image']

class EmailForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    attach = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))
    message = forms.CharField(widget=forms.Textarea)

class createDiscrepancyForm(forms.ModelForm):
    discrepancy_creation_date = forms.DateField(widget=DatePickerInput)
    class Meta:
        model = discrepancy_report
        fields = ['discrepancy_id', 'service_ord', 'cause_of_delay', 'discrepancy_creation_date', 'expected_delay_duration']    

class createJobForm(forms.ModelForm):
    date_in = forms.DateField(widget=DatePickerInput)
    required_start_date = forms.DateField(widget=DatePickerInput)
    required_end_date = forms.DateField(widget=DatePickerInput)
    class Meta:
        model = Ip220610Cleaned
        fields = ['date_in', 'required_start_date', 'required_end_date', 'service_ord', 'priority', 'ctat']
    
class createApprovalForWorkForm(forms.ModelForm):
    approval_creation_date = forms.DateField(widget=DatePickerInput)
    class Meta:
        model = approval_for_work
        fields = ['approval_creation_date', 'AFW_id', 'service_ord', 'discrepancy_id','AFW_status']

class createJobUpdateStartForm(forms.ModelForm):
    start_date_input = forms.DateTimeField(widget=DatePickerInput)
    start_date_actual = forms.DateTimeField(widget=DatePickerInput)
    class Meta:
        model = JobUpdateStart
        fields = ['job_update_id','service_ord','cause_of_delay', 'start_date_actual', 'start_date_actual']

class createJobUpdateEndForm(forms.ModelForm):
    end_date_input = forms.DateTimeField(widget=DatePickerInput)
    end_date_actual = forms.DateTimeField(widget=DatePickerInput)
    class Meta:
        model = JobUpdateEnd
        fields = ['service_ord', 'job_update_id', 'end_date_actual', 'end_date_input']

class createJobUpdateCompleteForm(forms.ModelForm):
    mal_end_date = forms.DateTimeField(widget=DatePickerInput)
    job_complete_input = forms.DateTimeField(widget=DatePickerInput)
    class Meta:
        model = JobUpdateComplete
        fields = ['service_ord', 'mal_end_date', 'job_complete_input']

# class CreateUserForm(UserCreationForm):
#     def clean(self):
#         cleaned_data = super(CreateUserForm, self).clean()

#         username = cleaned_data.get('username')
#         if username and User.objects.filter(username__iexact=username).exists():
#             self.add_error(
#                 'username', 'A user with that username already exists.')

#         email = cleaned_data.get('email')
#         if email and User.objects.filter(email__iexact=email).exists():
#             self.add_error(
#                 'email', 'A user with that email already exists.')

#         return cleaned_data

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
