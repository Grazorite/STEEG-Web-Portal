from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Order, NonFBReport, FBReport, CovidReport, NonFBChecklist, CovidComplianceChecklist, FBChecklist, steeg_user, job_status, equipment_inventory, approval_for_work, discrepancy_report


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
    class Meta:
        model = discrepancy_report
        fields = ['discrepancy_id', 'service_order_number', 'cause_of_delay', 'expected_delay_duration']

class createJobForm(forms.ModelForm):
    class Meta:
        model = job_status
        fields = ['service_order_number', 'employment_id', 'approval_status', 'priority']

class createApprovalForWorkForm(forms.ModelForm):
    class Meta:
        model = approval_for_work
        fields = ['AFW_id', 'service_order_number', 'employment_id', 'AFW_status']

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
