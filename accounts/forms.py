from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *
from .widgets import DatePickerInput, DateTimePickerInput

###############################CREATE NEW USER################################################
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


class createJobForm(forms.ModelForm):
    mal_start = forms.DateField(widget=DatePickerInput)
    required_start_date = forms.DateField(widget=DatePickerInput)
    required_end_date = forms.DateField(widget=DatePickerInput)
    class Meta:
        model = Maintable
        fields = [
            'service_order', 'priority_text', 'approval_status', 'mal_start', 'required_start_date', 'required_end_date',
            'customer_po_number','initial_po_number', 'mo_number', 'model_number', 'serial_no',
            'equipment_description', 'main_work_center', 'enduser', 'reported_fault_long_text', 
            'service_order_user_status','notification_user_status', 'mat', 'capacity_hour','ctat', 'calculated_ctat'
            ]
        widgets = {
            'service_order': forms.NumberInput(attrs={'class': 'form-control'}),
            'service_order_user_status': forms.TextInput(attrs={'class': 'form-control'}),
            'notification_user_status': forms.TextInput(attrs={'class': 'form-control'}),
            'priority_text': forms.Select(attrs={'class': 'form-control'}),
            'mat': forms.TextInput(attrs={'class': 'form-control'}),
            'approval_status': forms.Select(attrs={'class': 'form-control'}),
            'customer_po_number': forms.TextInput(attrs={'class': 'form-control'}),
            'initial_po_number': forms.TextInput(attrs={'class': 'form-control'}),
            'mo_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'model_number': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_no': forms.TextInput(attrs={'class': 'form-control'}),
            'equipment_description': forms.TextInput(attrs={'class': 'form-control'}),
            'reported_fault_long_text': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity_hour': forms.NumberInput(attrs={'class': 'form-control'}),
            'enduser': forms.TextInput(attrs={'class': 'form-control'}),
            'main_work_center': forms.Select(attrs={'class': 'form-control'}),
            'ctat': forms.NumberInput(attrs={'class': 'form-control'}),
            'calculated_ctat': forms.TextInput(attrs={'class': 'form-control'})
        }


class createJobUpdateStartForm(forms.ModelForm):
    start_date_input = forms.DateField(widget=DatePickerInput)
    start_date_actual = forms.DateField(widget=DatePickerInput)
    class Meta:
        model = Jobupdatestart
        fields = ['service_order', 'job_update_id', 'start_date_actual', 'start_date_input']
        widgets = {
            'job_update_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'service_order': forms.Select(attrs={'class': 'form-control'})
        }

class createJobUpdateEndForm(forms.ModelForm):
    end_date_input = forms.DateField(widget=DatePickerInput)
    end_date_actual = forms.DateField(widget=DatePickerInput)
    class Meta:
        model = Jobupdateend
        fields = ['service_order', 'job_update', 'end_date_actual', 'end_date_input', 'cause_of_delay']
        widgets = {
            'job_update': forms.Select(attrs={'class': 'form-control'}),
            'service_order': forms.Select(attrs={'class': 'form-control'}),
            'cause_of_delay': forms.Select(attrs={'class': 'form-control'})
        }
        

class createJobUpdateCompleteForm(forms.ModelForm):
    mal_end_date = forms.DateField(widget=DatePickerInput)
    job_complete_input = forms.DateField(widget=DatePickerInput)
    class Meta:
        model = Jobupdatecomplete
        fields = ['service_order', 'job_complete_id', 'mal_end_date', 'job_complete_input']
        widgets = {
            'job_update_id': forms.Select(attrs={'class': 'form-control'}),
            'service_order': forms.Select(attrs={'class': 'form-control'})
        }


class createApprovalForWorkForm(forms.ModelForm):
    approval_creation_date = forms.DateField(widget=DatePickerInput)
    class Meta:
        model = approval_for_work
        fields = ['approval_creation_date', 'AFW_id', 'service_order', 'discrepancy_id','AFW_status']
        widgets = {
            'AFW_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'service_order': forms.Select(attrs={'class': 'form-control'}),
            'discrepancy_id': forms.Select(attrs={'class': 'form-control'}),
            'AFW_status': forms.TextInput(attrs={'class': 'form-control'})
        }


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
        fields = ['discrepancy_id', 'service_order', 'cause_of_delay', 'discrepancy_creation_date', 'expected_delay_duration']  
        widgets = {
            'service_order': forms.Select(attrs={'class': 'form-control'}),
            'discrepancy_id': forms.TextInput(attrs={'class': 'form-control'}),
            'cause_of_delay': forms.Select(attrs={'class': 'form-control'}),
            'expected_delay_duration': forms.NumberInput(attrs={'class': 'form-control'})
        }  
