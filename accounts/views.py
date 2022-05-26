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
from .models import AuditScore
# Create your views here.


@login_required(login_url='login')
def home(request):
    orders = Order.objects.all()
    stores = Store.objects.all()

    total_orders = orders.count()
    pending = orders.filter(Q(status='Pending') | Q(
        status='Notification Sent')).count()

    context = {'orders': orders, 'stores': stores, 'pending': pending}
    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
def stores(request):
    stores = Store.objects.all()

    return render(request, 'accounts/stores.html', {'stores': stores})


@login_required(login_url='login')
def reports(request):
    reports = NonFBReport.objects.all()
    print(reports)
    # TODO: fix total_score
    #total_score = reports.compliance.all()
    total_score = 0
    print(total_score)

    context = {'reports': reports, 'total_score': total_score}
    return render(request, 'accounts/reports.html', context)

# def statistics_page(request):
#     statistics_page = Statistics_page.objects.all()
#     return render(request, 'accounts/stats.html', {'statistics_page': statistics_page})


@login_required(login_url='login')
def announcements(request):
    announcements = Announcement.objects.all()
    return render(request, 'accounts/announcements.html', {'announcements': announcements})

# @user_passes_test(lambda u: u.is_superuser)
# def send_email(request):
#         form = EmailForm()
#         if request.method == 'POST':
#             form = EmailForm(request.POST, request.FILES)
#             if form.is_valid():
#                 subject = request.POST.get('subject')
#                 message = request.POST.get('message')
#                 recipient = form.cleaned_data.get('email')
#                 upload = request.FILES['upload']
#                 send_mail(subject,
#                 message, settings.EMAIL_HOST_USER, [recipient], fail_silently=True)
#                 messages.success(request, 'Success!')
#                 return redirect('/')

#                 try:
#                     mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
#                     mail.attach(attach.name, attach.read(), attach.content_type)
#                     mail.send()
#                     return render(request, self.template_name, {'email_form': form, 'error_message': 'Sent email to %s'%email})
#                 except:
#                     return render(request, self.template_name, {'email_form': form, 'error_message': 'Either the attachment is too big or corrupt'})

#         return render(request, 'accounts/send_email.html', {'form': form})


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
def registerTenantPage(request):
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

            group = Group.objects.get(name='tenant')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/registerTenant.html', context)


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
def createRectification(request):
    if request.method == 'POST':
        form = RectifyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RectifyForm()
    context = {'form': form}
    return render(request, 'accounts/rectify_form.html', context)


@login_required(login_url='login')
def createNonFBReport(request):
    if request.method == 'POST':

        form = CreateNonFBReportForm(request.POST, request.FILES)
        if form.is_valid():
            # uploaded_file = request.FILES['file']
            # instance.save()
            form.save()
            return redirect('/')

    else:
        form = CreateNonFBReportForm()
    context = {'form': form, 'pageTitle': 'Report — non-F&B'}
    return render(request, 'accounts/createReport_form.html', context)


@login_required(login_url='login')
def createFBReport(request):
    if request.method == 'POST':

        form = CreateFBReportForm(request.POST, request.FILES)
        if form.is_valid():
            # uploaded_file = request.FILES['file']
            # instance.save()
            form.save()
            return redirect('/')

    else:
        form = CreateFBReportForm()
    context = {'form': form, 'pageTitle': 'Report — F&B'}
    return render(request, 'accounts/createReport_form.html', context)


@login_required(login_url='login')
def createCovidReport(request):
    if request.method == 'POST':

        form = CreateCovidReportForm(request.POST, request.FILES)
        if form.is_valid():
            # uploaded_file = request.FILES['file']
            # instance.save()
            form.save()
            return redirect('/')

    else:
        form = CreateCovidReportForm()
    context = {'form': form, 'pageTitle': 'Report — Covid Compliance'}
    return render(request, 'accounts/createReport_form.html', context)


class AccountChartView(TemplateView):
    template_name = 'accounts/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = AuditScore.objects.all()
        return context


@login_required(login_url='login')
def accessRestricted(request):
    return render(request, 'accounts/restricted.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def testAccess(request):
    return render(request, 'accounts/dashboard.html')
