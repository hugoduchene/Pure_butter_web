from django.test import SimpleTestCase
from substitute.forms import SearchSubstitute, SearchMeat

class TestForms(SimpleTestCase):

    def test_searchSubstitute(self):
        form = SearchSubstitute(data = {
            'input_product_name': 'nutella'
        })
        self.assertTrue(form.is_valid())

    def test_searchSubstitute_no_data(self):
        form = SearchSubstitute(data = {
                'input_product_name': ''
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_search_meat(self):
        form = SearchMeat(data = {
            'input_product_name' : 'nutella'

        })
        self.assertTrue(form.is_valid())

    def test_search_meat_no_data(self):
        form = SearchMeat(data = {
            'input_product_name' : ''
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
