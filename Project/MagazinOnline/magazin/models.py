from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        related_name='products',
    )
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00)], default=0.00)
    image = models.ImageField(upload_to='magazin', null=True, default=None)

    def get_stock_total_value(self):
        return self.quantity * float(self.price)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100, null=False, default=None)
    shipping_address = models.CharField(max_length=255, null=False, default=None)
    billing_address = models.CharField(max_length=255, null=True, default=None)
    email = models.EmailField(max_length=255, null=False, default=None)
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00)], default=0.00)
    products = models.ManyToManyField(Products, through='OrderProduct', related_name='orders')


class OrderProduct(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, default=None)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
