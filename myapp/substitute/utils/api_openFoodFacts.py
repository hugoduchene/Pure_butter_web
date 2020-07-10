import json
import urllib.request

class ApiOpenFoodFacts():
    """docstring forApiOpenFoodFacts."""

    def __init__(self):
        self.list_product = []
        self.list_categories = []


    def load_json(self):
        """ method for loading categories """

        url = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&sort_by=unique_scans_n&page_size=1000&page=1&json=true&field=products_name_fr.json"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())

        return data

    def get_categories(self):
        set_categories = set()
        data = self.load_json()
        for items in data["products"]:
            categories = items.get("categories", "")
            first_categories = categories.split(",")[0]
            set_categories.add(first_categories)
        return set_categories

    def get_data(self):
            """ method for taking the we need from json """
            data = self.load_json()

            for items in data["products"]:
                name_product = items.get('product_name_fr', "")
                stores = items.get('stores', "")
                description = items.get("ingredients_text_fr", "")
                score = items.get("nutrition_grades", "")
                brand = items.get("brands", "")
                link = items.get("url", "")
                picture = items.get("image_small_url", "")
                category = items.get('categories', "")
                parse_category = category.split(",")[0]

                dictionary_product = {
                    'category' : parse_category,
                    'product_name': name_product,
                    'ingredients': description,
                    'score_grade': score,
                    'stores': stores,
                    'brands': brand,
                    'link': link,
                    'pictures' : picture
                    }

                self.list_product.append(dictionary_product)

            return self.list_product
