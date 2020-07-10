from django.db import models

# Create your models here.


class Categories(models.Model):
    name_category = models.CharField(max_length=200, unique=True)

class Products(models.Model):
    id_category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200, unique=True)
    ingredients = models.TextField()
    score_grade = models.CharField(max_length=3)
    stores = models.CharField(max_length=200)
    brands = models.TextField()
    link = models.TextField()
    pictures = models.CharField(max_length=200, default="")

class User(models.Model):
    pseudo = models.CharField(max_length=155)
    password = models.CharField(max_length=200)
    mail = models.EmailField()

class User_record(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Products, on_delete=models.CASCADE)
