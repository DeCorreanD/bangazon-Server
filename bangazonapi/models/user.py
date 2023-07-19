from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=100)
    image = models.URLField()
    uid = models.CharField(max_length=100)
    isseller = models.BooleanField(null=True, blank=True)
