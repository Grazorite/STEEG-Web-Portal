from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Order, MainDB, Jobupdatestart, Jobupdateend, Jobupdatecomplete, steeg_user, equipment_inventory, approval_for_work, discrepancy_report
from .widgets import DatePickerInput, DateTimePickerInput

class RectifyForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['store', 'Non_FB_Report', 'FB_Report',
                  'Covid_Compliance_Report', 'upload_image']

class CreateUserForm(UserCreationForm):
    def clean(self):
        cleaned_data = super(CreateUserForm, self).clean()

        username = cleaned_data.get('username')
        if username and User.objects.filter(username__iexact=username).exists():
            self.add_error(
                'username', 'A user with that username already exists.')

        email = cleaned_data.get('email')
        if email and User.objects.filter(email__iexact=email).exists():
            self.add_error(
                'email', 'A user with that email already exists.')

        return cleaned_data

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

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
        model = MainDB
        fields = [
            'service_ord','service_order_user_status','notification_user_status',
            'priority', 'mat','ctat', 'customer_po_number',
            'initial_po_number', 'mo_number',
            'equipment_description', 'model_number',
            'date_in', 'required_start_date', 'required_end_date',
            'reported_fault_long_text', 'capacity_hour', 'enduser',
            'main_work_center', 'ctat', 'calculated_ctat'
            ]
    
class createApprovalForWorkForm(forms.ModelForm):
    approval_creation_date = forms.DateField(widget=DatePickerInput)
    class Meta:
        model = approval_for_work
        fields = ['approval_creation_date', 'AFW_id', 'service_ord', 'discrepancy_id','AFW_status']

class createJobUpdateStartForm(forms.ModelForm):
    start_date_input = forms.DateTimeField(widget=DatePickerInput)
    start_date_actual = forms.DateTimeField(widget=DatePickerInput)
    class Meta:
        model = Jobupdatestart
        fields = ['job_update_id','service_ord','cause_of_delay', 'start_date_actual', 'start_date_input']

class createJobUpdateEndForm(forms.ModelForm):
    end_date_input = forms.DateTimeField(widget=DatePickerInput)
    end_date_actual = forms.DateTimeField(widget=DatePickerInput)
    class Meta:
        model = Jobupdateend
        fields = ['service_order', 'job_update', 'end_date_actual', 'end_date_input']

class createJobUpdateCompleteForm(forms.ModelForm):
    mal_end_date = forms.DateTimeField(widget=DatePickerInput)
    job_complete_input = forms.DateTimeField(widget=DatePickerInput)
    class Meta:
        model = Jobupdatecomplete
        fields = ['service_order', 'mal_end_date', 'job_complete_input', 'job_update_id']

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
