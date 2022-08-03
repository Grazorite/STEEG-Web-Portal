import contextlib
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.views import View
from django.views.generic import TemplateView
from .filters import *
import csv
# Create your views here.

@login_required(login_url='login')
def home(request):
    maintable_jobs = Maintable.objects.all()
    total_maintable_jobs = maintable_jobs.count()
    pending_jobs = maintable_jobs.filter(approval_status = 'Pending')
    total_pending_jobs = pending_jobs.count()
    context = {
            'maintable_jobs': maintable_jobs, 
            'total_maintable_jobs': total_maintable_jobs,
            'pending_jobs': pending_jobs, 
            'total_pending_jobs': total_pending_jobs,
            }

    return render(request, 'accounts/home.html', context)


@login_required(login_url='login')
def jobs(request):
    maintable_jobs = Maintable.objects.all()
    total_maintable_jobs = maintable_jobs.count()
    pending_jobs = maintable_jobs.filter(approval_status = 'Pending')
    total_pending_jobs = pending_jobs.count()
    context = {
            'maintable_jobs': maintable_jobs, 
            'total_maintable_jobs': total_maintable_jobs,
            'pending_jobs': pending_jobs, 
            'total_pending_jobs': total_pending_jobs,
            }

    return render(request, 'accounts/reports.html', context)


def dash(request):
    jobs = Maintable.objects.all()
    return render(request, 'accounts/dash.html', {'jobs': jobs})


@login_required(login_url='login')
def approvals(request):
    maintable_jobs = Maintable.objects.all()
    total_maintable_jobs = maintable_jobs.count()
    pending_jobs = maintable_jobs.filter(approval_status = 'Pending')
    total_pending_jobs = pending_jobs.count()
    approvals_filter = ApprovalFilter(request.GET, queryset=maintable_jobs)
    filtered = approvals_filter.qs
    total_filtered=len(filtered)

    context = {
        'maintable_jobs': maintable_jobs,
        'approvals_filter': approvals_filter,
        'total_maintable_jobs': total_maintable_jobs,
        'pending_jobs': pending_jobs,
        'total_pending_jobs': total_pending_jobs,
        'filtered': filtered,
        'total_filtered': total_filtered
        }

    return render(request, 'accounts/approvals.html', context)

@user_passes_test(lambda u: u.is_superuser)
def update_approval(request, service_order):
    approval = Maintable.objects.get(pk=service_order)
    form = createJobForm(request.POST or None, instance=approval)
    if form.is_valid():
        form.save()
        return redirect('approvals')
    
    context = {
        'approval': approval,
        'form': form
    }

    return render(request, 'accounts/update_approval.html', context)

@user_passes_test(lambda u: u.is_superuser)
def report_generation(request):
    completedJobs = Reportgeneration.objects.all()
    completed_job_filter = JobFilter(request.GET, queryset=completedJobs)
    maintable_jobs = Maintable.objects.all()
    total_maintable_jobs = maintable_jobs.count()
    pending_jobs = maintable_jobs.filter(approval_status = 'Pending')
    total_pending_jobs = pending_jobs.count()
    context = {
        'completedJobs': completedJobs,
        'completed_job_filter': completed_job_filter,
        'maintable_jobs': maintable_jobs,
        'total_maintable_jobs': total_maintable_jobs,
        'pending_jobs': pending_jobs,
        'total_pending_jobs': total_pending_jobs,
    }

    return render(request, 'accounts/report_generation.html', context)

def generate_report_csv(request):
    reportJobs = Reportgeneration.objects.all()
    search = JobFilter(request.GET, queryset= reportJobs).qs
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=completed_jobs.csv'

    # Create a csv writer
    writer = csv.writer(response)

    # Designate The Model
    writer.writerow([
        'SERVICE_ORDER', 'SYSTEM', 'MAT', 'PRIORITY_TEXT', 'MAL_START', 'MAL_END',
        'CTAT', 'TET', 'Out_By', 'ATAT', 'A_W_SPARE', 'A_W_FACILITY', 'A_W_OTHER_JOB',
        'INST', 'OTH', 'AWAIT_UNIT_ACCEPT', 'MULTIPLE_FAULTS', 'REMARKS', 
        'EQUIPMENT_DESCRIPTION', 'MODEL_NUMBER', 'SERIAL_NO', 'Reported_Fault_Long_Text'
        ])

    #Loop Through Queryset
    for i in search:
        writer.writerow([
            i.service_order, i.system, i.mat, i.priority_text, i.mal_start,
            i.mal_end, i.ctat, i.tet, i.out_by, i.atat, i.a_w_spare, i.a_w_facility,
            i.a_w_other_job, i.inst, i.oth, i.await_unit_accept, i.multiple_faults,
            i.remarks, i.equipment_description, i.model_number, i.serial_no, i.reported_fault_long_text
        ])

    return response
# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])

@unauthenticated_user
def registerPage(request):
    return render(request, 'accounts/register.html')


@unauthenticated_user
def registerEngineerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username').lower()
            email = form.cleaned_data.get('email').lower()

            brk = True

            try:
                User.objects.get(username__iexact=username)
            except:
                brk = False

            if brk:
                messages.warning(request, 'Username already in use')
                return redirect('login')

            user = form.save()

            group = Group.objects.get(name='Engineer')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/registerEngineer.html', context)


@unauthenticated_user
def registerDstarPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username').lower()
            email = form.cleaned_data.get('email').lower()

            brk = True

            try:
                User.objects.get(username__iexact=username)
            except:
                brk = False

            if brk:
                messages.warning(request, 'Username already in use')
                return redirect('login')

            user = form.save()

            group = Group.objects.get(name='DSTAR')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/registerDstar.html', context)


@unauthenticated_user
def registerRsafPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username').lower()
            email = form.cleaned_data.get('email').lower()

            brk = True

            try:
                User.objects.get(username__iexact=username)
            except:
                brk = False

            if brk:
                messages.warning(request, 'Username already in use')
                return redirect('login')

            user = form.save()

            group = Group.objects.get(name='RSAF')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/registerRsaf.html', context)

@unauthenticated_user
def registerAdminPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username').lower()
            email = form.cleaned_data.get('email').lower()

            brk = True

            try:
                User.objects.get(username__iexact=username)
            except:
                brk = False

            if brk:
                messages.warning(request, 'Username already in use')
                return redirect('login')

            user = form.save()

            group = Group.objects.get(name='admin')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/registerAdmin.html', context)


@unauthenticated_user
@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def createDiscrepancy(request):
    if request.method == 'POST':

        form = createDiscrepancyForm(request.POST, request.FILES)
        if form.is_valid():
            # uploaded_file = request.FILES['file']
            # instance.save()
            form.save()
            return redirect('/')

    else:
        form = createDiscrepancyForm()
    context = {'form': form, 'pageTitle': 'Job Discrepancy Report'}
    return render(request, 'accounts/createReport_form.html', context)


@login_required(login_url='login')
def createJob(request):
    if request.method == 'POST':

        form = createJobForm(request.POST, request.FILES)
        if form.is_valid():
            # uploaded_file = request.FILES['file']
            # instance.save()
            form.save()
            return redirect('/')

    else:
        form = createJobForm()
    context = {'form': form, 'pageTitle': 'Job Creation Form'}
    return render(request, 'accounts/createReport_form.html', context)


@login_required(login_url='login')
def createApprovalForWork(request):
    if request.method == 'POST':

        form = createApprovalForWorkForm(request.POST, request.FILES)
        if form.is_valid():
            # uploaded_file = request.FILES['file']
            # instance.save()
            form.save()
            return redirect('/')

    else:
        form = createApprovalForWorkForm()
    context = {'form': form, 'pageTitle': 'Approval For Work'}
    return render(request, 'accounts/createReport_form.html', context)

@login_required(login_url='login')
def createJobUpdateStart(request):
    if request.method == 'POST':

        form = createJobUpdateStartForm(request.POST, request.FILES)
        if form.is_valid():
            # uploaded_file = request.FILES['file']
            # instance.save()
            form.save()
            return redirect('/')

    else:
        form = createJobUpdateStartForm()
    context = {'form': form, 'pageTitle': 'Job Update Start'}
    return render(request, 'accounts/createReport_form.html', context)


@login_required(login_url='login')
def createJobUpdateEnd(request):
    if request.method == 'POST':

        form = createJobUpdateEndForm(request.POST, request.FILES)
        if form.is_valid():
            # uploaded_file = request.FILES['file']
            # instance.save()
            form.save()
            return redirect('/')

    else:
        form = createJobUpdateEndForm()
    context = {'form': form, 'pageTitle': 'Job Update End'}
    return render(request, 'accounts/createReport_form.html', context)

@login_required(login_url='login')
def createJobUpdateComplete(request):
    if request.method == 'POST':

        form = createJobUpdateCompleteForm(request.POST, request.FILES)
        if form.is_valid():
            # uploaded_file = request.FILES['file']
            # instance.save()
            form.save()
            return redirect('/')

    else:
        form = createJobUpdateCompleteForm()
    context = {'form': form, 'pageTitle': 'Job Completion'}
    return render(request, 'accounts/createReport_form.html', context)

@login_required(login_url='login')
def accessRestricted(request):
    return render(request, 'accounts/restricted.html')
