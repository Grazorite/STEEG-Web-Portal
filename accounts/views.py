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
# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    jobs = MainDB.objects.all()
    return render(request, 'accounts/dashboard.html', {'jobs': jobs})

@login_required(login_url='login')
def home(request):
    ip_jobs = MainDB.objects.all()
    total_ip_jobs = ip_jobs.count()
    approvals = approval_for_work.objects.all()
    total_approvals = approvals.count()
    context = {'ip_jobs': ip_jobs, 'total_ip_jobs': total_ip_jobs,
                'approvals': approvals, 'total_approvals': total_approvals}
    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def jobs(request):
    ip_jobs = MainDB.objects.all()
    total_ip_jobs = ip_jobs.count()
    approvals = approval_for_work.objects.all()
    total_approvals = approvals.count()
    context = {'ip_jobs': ip_jobs, 'total_ip_jobs': total_ip_jobs,
                'approvals': approvals, 'total_approvals': total_approvals}
    
    return render(request, 'accounts/reports.html', context)

def dash(request):
    jobs = MainDB.objects.all()
    return render(request, 'accounts/dashboard.html', {'jobs': jobs})


@login_required(login_url='login')
def approvals(request):
    approvals = approval_for_work.objects.all()
    return render(request, 'accounts/approvals.html', {'approvals': approvals})

@user_passes_test(lambda u: u.is_superuser)
def send_email(request):
        form = EmailForm()
        if request.method == 'POST':
            form = EmailForm(request.POST, request.FILES)
            if form.is_valid():
                subject = request.POST.get('subject')
                message = request.POST.get('message')
                recipient = form.cleaned_data.get('email')
                upload = request.FILES['upload']
                send_mail(subject,
                message, settings.EMAIL_HOST_USER, [recipient], fail_silently=True)
                messages.success(request, 'Success!')
                return redirect('/')

                try:
                    mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
                    mail.attach(attach.name, attach.read(), attach.content_type)
                    mail.send()
                    return render(request, self.template_name, {'email_form': form, 'error_message': 'Sent email to %s'%email})
                except:
                    return render(request, self.template_name, {'email_form': form, 'error_message': 'Either the attachment is too big or corrupt'})

        return render(request, 'accounts/send_email.html', {'form': form})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def EmailAttachementView(request):
    form = EmailForm(request.POST, request.FILES)
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        email = form.cleaned_data['email']
        files = request.FILES.getlist('attach')
        try:
            mail = EmailMessage(
                subject, message, settings.EMAIL_HOST_USER, [email])
            for f in files:
                mail.attach(f.name, f.read(), f.content_type)
            mail.send()
            return redirect('/')
            return render(request, 'accounts/send_email.html', {'form': form, 'error_message': 'Sent email to %s' % email})
        except:
            return render(request, 'send_email.html', {'form': form, 'error_message': 'Either the attachment is too big or corrupt'})
    return render(request, 'accounts/send_email.html', {'form': form, 'error_message': 'Unable to send email. Please try again later'})


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


# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
# def testAccess(request):
#     return render(request, 'accounts/dashboard.html')
