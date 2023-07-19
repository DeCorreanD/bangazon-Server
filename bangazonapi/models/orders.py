from django.db import models
from .user import User


class Orders(models.Model):
    closed = models.BooleanField(null=True, blank=True)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
