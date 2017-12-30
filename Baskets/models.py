from django.contrib.auth.models import User
from django.db import models
from Products.models import Product


class ElementBasket(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    count = models.IntegerField('Количество товара')
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return '%s, %s' % (self.product, self.count)
