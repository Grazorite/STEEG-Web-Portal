from django.test import TestCase, Client
from django.contrib.auth.models import User, Permission
from django.urls import reverse
from accounts.models import steeg_user, job_status, equipment_inventory, approval_for_work, discrepancy_report
import json

class TestViews(TestCase):
    '''
    these are unit tests to ensure that each view and its related classes are working
    login is required in setUp else the subsequent views will return HTTP 302: redirect error
    to run: $ python manage.py test accounts
    '''
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
        
        self.login_url = reverse('login')
        self.announcements_url = reverse('announcements')
        self.reports_url = reverse('reports')
        self.chart_url = reverse('chart')
        
    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now, copy-paste above code for each test case below
        self.assertTrue(response.context['user'].is_active)

    def test_login_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
    
    def test_announcements_GET(self):
        response = self.client.post('/login/', self.credentials, follow=True)

        response = self.client.get(self.announcements_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/announcements.html')
    
    def test_reports_GET(self):
        response = self.client.post('/login/', self.credentials, follow=True)

        response = self.client.get(self.reports_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/reports.html')
    
    def test_chart_GET(self):
        response = self.client.post('/login/', self.credentials, follow=True)

        response = self.client.get(self.chart_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/chart.html')
