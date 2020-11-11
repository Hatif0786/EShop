from django.db import models

class Product_s(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to="products/")