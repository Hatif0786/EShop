from django.db import models

class Customer(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        else:
            return False