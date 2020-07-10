from django.core.management.base import BaseCommand, CommandError
from substitute.models import Products, Categories
from substitute.utils.api_openFoodFacts import ApiOpenFoodFacts
from django.shortcuts import render, get_object_or_404

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        api_off = ApiOpenFoodFacts()

        categories = api_off.get_categories()

        for items in categories:
            req_category, created = Categories.objects.get_or_create(name_category = items)
            req_category.save()

        list_dict_product = api_off.get_data()
        for i in list_dict_product:
            category_product = i.get("category")
            id_category = get_object_or_404(Categories, name_category = category_product)
            if len(Products.objects.filter(product_name = i.get("product_name"))):
                pass
            else:
                req_product, created = Products.objects.get_or_create(
                    id_category = id_category,
                    product_name = i.get('product_name'),
                    ingredients = i.get('ingredients'),
                    score_grade = i.get('score_grade'),
                    stores = i.get('stores'),
                    brands = i.get('brands'),
                    link = i.get('link'),
                    pictures = i.get('pictures')
                )
                req_product.save()
