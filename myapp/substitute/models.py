from django.db import models


# Create your models here.
class Categories(models.Model):
    name_category = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name_category

class Products(models.Model):
    id_category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200, unique=True)
    ingredients = models.TextField()
    score_grade = models.CharField(max_length=3)
    stores = models.CharField(max_length=200)
    brands = models.TextField()
    link = models.TextField()
    pictures = models.CharField(max_length=200, default="")
    nutrition_score_100 = models.IntegerField(null=True)

    def __str__(self):
        return self.product_name

class User_record(models.Model):
    id_user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE)
    id_product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_product
