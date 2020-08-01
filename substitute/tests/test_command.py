from django.test import TestCase, Client
from django.core import mail
from django.core.management import call_command
from substitute.management.commands.send_email import Command
from user.models import UserSubscribeEmail, CustomUser
from substitute.models import Products, Categories

class TestCommand(TestCase):

    def setUp(self):
        self.list_categories = ['boisson', 'tartine', 'sandwich', 'viande']
        self.list_products = ['coca', 'tartine nutella', 'club', 'entrecote']
        self.command = Command()
        self.login = CustomUser(username='hugo', email='hugo@hotmail.com', password='mlkjhg1234')
        self.login.save()

    def test_get_email_user_subscribe(self):
        UserSubscribeEmail(id_user=self.login).save()
        self.command.get_email_user_subscribe()
        self.assertEquals(self.command.list_email, ['hugo@hotmail.com'])

    def test_get_random_products(self):
        for i in range(3):
            category = Categories(name_category=self.list_categories[i])
            category.save()
            Products(id_category=category, product_name=self.list_products[i]).save()

        self.command.get_random_products()
        self.command.text_content()

        self.assertEquals(len(self.command.txt.split('\n')), 4)
        self.assertEquals(len(self.command.list_products), 3)
        self.assertEquals(len(self.command.list_categories), 3)

    def test_send_all_email(self):
        self.command.list_email = ['hugo@gmail.com']
        msg = ('Toujours pleins de substituants chez PureButterWeb', "ahahahah", 'a@gmail.com' , self.command.list_email)
        mail.send_mass_mail((msg, ), fail_silently=False)

        self.assertEquals(len(mail.outbox), 1)
