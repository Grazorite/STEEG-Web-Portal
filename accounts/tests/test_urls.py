# from django.test import SimpleTestCase
# from django.urls import reverse, resolve
# from accounts.views import home, jobs, reports, announcements, accessRestricted, loginPage, registerAdminPage, registerTenantPage, registerPage, logoutUser, createDiscrepancy, createJob, createApprovalForWork, createRectification, AccountChartView

# class TestUrls(SimpleTestCase):
#     '''
#     these are unit tests to ensure that every single url is working. follows format of accounts/urls.py
#     to run: $ python manage.py test accounts
#     '''
#     # main
#     def test_home_url_is_resolved(self):
#         url = reverse('home')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, home)
        
#     def test_jobs_url_is_resolved(self):
#         url = reverse('jobs')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, jobs)
        
#     def test_reports_url_is_resolved(self):
#         url = reverse('reports')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, reports)
        
#     def test_announcements_url_is_resolved(self):
#         url = reverse('announcements')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, announcements)
        
#     def test_restricted_url_is_resolved(self):
#         url = reverse('restricted')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, accessRestricted)
        
#     # user access
#     def test_login_url_is_resolved(self):
#         url = reverse('login')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, loginPage)
        
#     def test_registerAdmin_url_is_resolved(self):
#         url = reverse('registeradmin')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, registerAdminPage)
        
#     def test_registerTenant_url_is_resolved(self):
#         url = reverse('registertenant')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, registerTenantPage)
        
#     def test_registerPage_url_is_resolved(self):
#         url = reverse('register')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, registerPage)
    
#     def test_logout_url_is_resolved(self):
#         url = reverse('logout')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, logoutUser)
        
#     # forms
#     def test_discrepancyForm_url_is_resolved(self):
#         url = reverse('createDiscrepancy_form')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, createDiscrepancy)
        
#     def test_jobForm_url_is_resolved(self):
#         url = reverse('createJob_form')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, createJob)
        
#     def test_approvalForWorkForm_url_is_resolved(self):
#         url = reverse('createApprovalForWork_form')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, createApprovalForWork)
        
#     def test_rectifyForm_url_is_resolved(self):
#         url = reverse('rectify_form')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, createRectification)
        
#     # charts
#     def test_accountChartView_url_is_resolved(self):
#         url = reverse('chart')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func.view_class, AccountChartView)

