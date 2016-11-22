from django.db import models

# Create your models here.

class Coffee(models.Model):
    name = models.CharField(default='', max_length=200)
    price = models.DecimalField(null=True, decimal_places=2, max_digits=4)
    stock = models.IntegerField(default=0)