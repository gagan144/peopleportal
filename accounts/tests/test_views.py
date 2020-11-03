from django.test import TestCase, Client
from django.urls import reverse


class TestAccountViews(TestCase):

    def setUp(self):
        self.client = Client()

    # ----- Login/Logout -----
    def test_loginPage_GET(self):
        response = self.client.get(reverse('accounts__login'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    # ----- /Login/Logout -----


    # ----- Employess CRUD -----
    def test_employeeCRUDViews_noAuth(self):
        list_urls = [
            reverse('accounts__api_employee_delete'),
            reverse('accounts__api_employee_create'),
            reverse('accounts__api_employee_edit'),
        ]

        for url in list_urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302, msg=f"Insecure view '{url}'. Not redirecting to login!")


    # ----- Employess CRUD -----


    # ----- Resources -----
    def test_apiEmployees_noAuth_GET(self):
        response = self.client.get("/accounts/api/employees/?format=json")

        self.assertEqual(response.status_code, 401)

    # ----- /Resources -----
