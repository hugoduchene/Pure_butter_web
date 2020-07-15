from django.test import SimpleTestCase
from django.urls import reverse, resolve
from user.views import accountView, registrationView

class testUrls(SimpleTestCase):

    def test_registrer_view_url(self):
        url = reverse('registration')
        self.assertEquals(resolve(url).func, registrationView)

    def test_accountView_url(self):
        url = reverse('account')
        self.assertEquals(resolve(url).func, accountView)
