from django.db import models


class Cart(models.Model):

    products = models.ManyToManyField(
        'products.Product',
        verbose_name='محصول',
        blank=True
    )

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید'

    def __str__(self):
        return str(self.id)

    @property
    def total_price(self):
        total_price = 0
        for product in self.products.all():
            total_price += product.price
        return total_price
