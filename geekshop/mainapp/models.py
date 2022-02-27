from email.policy import default
from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя', max_length=64, unique=True, default='')
    image = models.ImageField(verbose_name='фото', default='')
    description = models.TextField(verbose_name='описание', blank=True, default='')
    date = models.DateTimeField(
        verbose_name='время создания', auto_now_add=True)
    price = models.DecimalField(
        verbose_name='стоимость', max_digits=8, decimal_places=2, default='')

def __str__(self):
    return f"{self.name} ({self.category.name})"
