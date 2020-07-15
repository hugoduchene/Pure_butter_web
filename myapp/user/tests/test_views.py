from django.test import TestCase, Client
from django.urls import reverse



class testViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.registration_url = reverse('registration')
        self.account_url = reverse('account')
        self.index_url = reverse('index')

    def test_account_GET(self):
        response = self.client.get(self.account_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/account.html')

    def test_registration_GET(self):
        response = self.client.get(self.registration_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/registration.html')

    def test_registration_POST(self):
        response = self.client.post(self.registration_url, {
            'username' : 'jk',
            'password1' : 'mlkjhg1234'
        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/registration.html')
