from django.test import TestCase
from substitute.models import Categories, Products, User_record
from django.contrib.auth import get_user_model


class TestModel(TestCase):

    def setUp(self):
        self.User = get_user_model()
        self.create_user = self.User.objects.create(
            username = 'jk',
            password = 'mlkjhg1234',
            email = 'a@gmai.com'
        )

        self.category = Categories.objects.create(
            name_category = 'eau'
        )

        self.product = Products.objects.create(
            id_category = self.category,
            product_name = "evian"
        )

        self.user_record = User_record.objects.create(
            id_user = self.create_user,
            id_product = self.product

        )

    def test_categories_is_good(self):
        self.assertEquals(self.category.name_category, 'eau')

    def test_products_is_good(self):
        self.assertEquals(self.product.product_name, 'evian')

    def test_User_record(self):
        self.assertEquals(self.user_record.id_product.id, self.product.id)
