from django.test import TestCase
from django.contrib.auth import get_user_model

class TestModelUser(TestCase):

    def setUp(self):
        self.User = get_user_model()

        self.create_user = self.User.objects.create(
            username = 'jk',
            password = 'mlkjhg1234',
            email = 'a@gmai.com'
        )

    def test_UserModel_is_good(self):
        self.assertEquals(self.create_user.username, 'jk')
