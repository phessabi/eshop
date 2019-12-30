from django.db import models


class Specification(models.Model):
    product = models.ForeignKey('products.Product',
                                on_delete=models.CASCADE,
                                verbose_name='محصول')
    field = models.ForeignKey('products.Field',
                              on_delete=models.CASCADE,
                              verbose_name='فیلد')
    value = models.CharField(max_length=1000,
                             verbose_name='مقدار')

    class Meta:
        verbose_name = 'مشخصات محصول'
        verbose_name_plural = 'مشخصات محصولات'

    def __str__(self):
        return str(self.product) + '-' + str(self.field) + '-' + self.value