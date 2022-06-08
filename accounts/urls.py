from django.urls import path
from . import views
from accounts.views import AccountChartView



urlpatterns = [
    path('', views.home, name='home'),
    path('stores/', views.stores, name='stores'),
    path('reports/', views.reports, name='reports'),
    path('announcements/', views.announcements, name='announcements'),
    path('restricted/', views.accessRestricted, name="restricted"),

    #email with file
    path('send_email/', views.EmailAttachementView, name='send_email'),
    # path('statistics_page/', views.statistics_page, name='statistics_page'),
    
    path('login/', views.loginPage, name='login'),
    path('register/admin/', views.registerAdminPage, name='registeradmin'),
    path('register/tenant/', views.registerTenantPage, name='registertenant'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),

    # forms
    path('createDiscrepancy_form/', views.createDiscrepancy, name='createDiscrepancy_form'),
    path('createJob_form/', views.createJob, name='createJob_form'),
    path('createApprovalForWork_form/', views.createApprovalForWork, name='createApprovalForWork_form'),
    path('rectify_form/', views.createRectification, name='rectify_form'),

    # charts
    path('chart/', AccountChartView.as_view(), name='chart'),

    # test (delete later)
    path('testAccess/', views.testAccess, name='testAccess'),
]
