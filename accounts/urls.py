from django.urls import path
from . import views


urlpatterns = [
    # main
    path('', views.home, name='home'),
    path('jobs/', views.jobs, name='jobs'),
    path('dash/', views.dash, name='dash'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('approvals/', views.approvals, name='approvals'),
    path('restricted/', views.accessRestricted, name="restricted"),
    path('generate_report_csv', views.generate_report_csv, name='generatereportcsv'),

    #email with file
    path('report_generation/', views.report_generation, name='report_generation'),
    # path('statistics_page/', views.statistics_page, name='statistics_page'),
    
    path('login/', views.loginPage, name='login'),
    path('register/admin/', views.registerAdminPage, name='registeradmin'),
    path('register/engineer/', views.registerEngineerPage, name='registerengineer'),
    path('register/dstar/', views.registerDstarPage, name='registerdstar'),
    path('register/rsaf/', views.registerRsafPage, name='registerrsaf'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),

    # forms
    path('createDiscrepancy_form/', views.createDiscrepancy, name='createDiscrepancy_form'),
    path('createJob_form/', views.createJob, name='createJob_form'),
    path('createApprovalForWork_form/', views.createApprovalForWork, name='createApprovalForWork_form'),
    path('createJobUpdateStart_form/', views.createJobUpdateStart, name='createJobUpdateStart_form'),
    path('createJobUpdateEnd_form/', views.createJobUpdateEnd, name='createJobUpdateEnd_form'),
    path('createJobUpdateComplete_form/', views.createJobUpdateComplete, name='createJobUpdateComplete_form'),
    path('update_approval/<service_order>', views.update_approval, name='updateapproval')

]
