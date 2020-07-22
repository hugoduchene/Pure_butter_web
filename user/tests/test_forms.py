from django.test import TestCase
from user.forms import RegistrationForm, LoginForm

class TestForms(TestCase):
    def test_registration_data(self):
        form = RegistrationForm(data = {
            'username' : 'jkpour',
            'email' : 'ahah@gmail.com',
            'password1' : 'mlkjhg1234',
            'password2' : 'mlkjhg1234'
        })
        self.assertTrue(form.is_valid())

    def test_Registration_no_data(self):
        form = RegistrationForm(data = {
            'username' : '',
            'email' : '',
            'password1' : '',
            'password2' : ''
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_login(self):
        form = LoginForm(data = {
            'username' : 'jk',
            'password' : 'mlkjhg1234'
        })
        self.assertTrue(form.is_valid())

    def test_login(self):
        form = LoginForm(data = {
            'username' : '',
            'password' : ''
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
