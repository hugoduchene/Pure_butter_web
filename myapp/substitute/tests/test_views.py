from django.test import TestCase, Client
from django.urls import reverse
from substitute.models import Categories, Products, User_record
from user.models import CustomUser as User


class testViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.result_url = reverse('result')
        self.search_meat_url = reverse('meat', args=['nutella'])
        self.Categories = Categories.objects.create(
            name_category='pate à tartiner'
        )
        self.product = Products.objects.create(
            id_category = self.Categories,
            product_name='nutella'
        )
        self.save_food_url = reverse('save')
        self.productRecord_url = reverse('myfood')



    def test_index_GET(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'substitute/index.html')

    def test_result_GET(self):
        response = self.client.get(self.result_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'substitute/404.html')

    def test_search_meat_GET(self):
        response = self.client.get(self.search_meat_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'substitute/food.html')

    def test_save_food_GET(self):
        response = self.client.get(self.save_food_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'substitute/404.html')

    def test_get_product_record(self):
        response = self.client.get(self.productRecord_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'substitute/myfood.html')

    def test_result_POST(self):
        response = self.client.post(self.result_url, {
            'input_product_name':'nutella'
        })
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'substitute/result.html')

    def test_save_food_POST(self):
        user = self.client.force_login(User.objects.get_or_create(username='testuser')[0])
        response = self.client.post(self.save_food_url, {
            'id_product' : self.product.id
        })

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.index_url, status_code=302)
