from django.db import models

class Customer(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=100)