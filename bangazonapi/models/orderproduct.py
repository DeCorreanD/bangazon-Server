from django.db import models
from .orders import Orders
from .product import Product

class OrderProduct(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
