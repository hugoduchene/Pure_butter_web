from django.test import TestCase, Client
from django.urls import reverse
from user.models import CustomUser as User
from user.forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm


class testViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.registration_url = reverse('registration')
        self.account_url = reverse('account')
        self.index_url = reverse('index')

    def test_account_GET_login(self):
        user = self.client.force_login(User.objects.get_or_create(username='testuser')[0])
        response = self.client.get(self.account_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/account.html')

    def test_account_GET(self):
        response = self.client.get(self.account_url)
        self.assertRedirects(response, self.registration_url, status_code=302)

    def test_registration_POST_form(self):
        form_data = {
            'username' : 'jkpour',
            'email' : 'maaaa@gmail.com',
            'password1' : 'mlkjhg1234',
            'password2' : 'mlkjhg1234'
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())
        response = self.client.post(self.registration_url, form_data)
        self.assertRedirects(response, self.index_url, status_code=302)


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
