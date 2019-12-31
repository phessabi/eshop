from django.db import models


class Product(models.Model):

    title = models.CharField(
        max_length=64,
        verbose_name='عنوان'
    )

    category = models.ForeignKey(
        'products.Category',
        on_delete=models.CASCADE,
        verbose_name='دسته'
    )

    image = models.ImageField(
        upload_to='resources/images/products',
        null=True,
        blank=True,
        verbose_name='تصویر'
    )

    price = models.CharField(
        max_length=50,
        verbose_name='قیمت'
    )

    express = models.BooleanField(
        default=False,
        verbose_name='فوری'
    )

    vendor = models.ForeignKey(
        'accounts.Vendor',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='فروشنده'
    )

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title
