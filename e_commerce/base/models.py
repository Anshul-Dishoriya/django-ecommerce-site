from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Cart(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)


class Order(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
