from django.db import models

class Product(models.Model):
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    status = models.BooleanField()

    def __str__(self):
        return self.name
    
