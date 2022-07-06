from django.urls import path
from . import views
from accounts.views import AccountChartView



urlpatterns = [
    # main
    path('', views.home, name='home'),
    path('jobs/', views.jobs, name='jobs'),
    path('reports/', views.reports, name='reports'),
    path('announcements/', views.announcements, name='announcements'),
    path('restricted/', views.accessRestricted, name="restricted"),
   
   # user access
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
    # path('testAccess/', views.testAccess, name='testAccess'),
]
