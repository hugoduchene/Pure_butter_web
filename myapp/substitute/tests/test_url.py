from django.test import SimpleTestCase
from django.urls import reverse, resolve
from substitute.views import get_product_record, save_food, search_meat, result, index

class TestUrls(SimpleTestCase):

    def test_myfood_url_is_resolved(self):
        url = reverse('myfood')
        self.assertEquals(resolve(url).func, get_product_record)

    def test_save_url_is_resolved(self):
        url = reverse('save')
        self.assertEquals(resolve(url).func, save_food)

    def test_meat_url_is_resolved(self):
        url = reverse('meat', args=['name_product'])
        self.assertEquals(resolve(url).func, search_meat)

    def test_result_url_is_resolved(self):
        url = reverse('result')
        self.assertEquals(resolve(url).func, result)

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)
