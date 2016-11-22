from django.db import models

# Create your models here.


class Kawa(models.Model):
    nazwa = models.CharField(default='', max_length=200)
    cena = models.DecimalField(null=True, decimal_places=2, max_digits=4)
    ilosc = models.IntegerField(default=0)