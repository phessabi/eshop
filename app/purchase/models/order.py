from django.db import models


class Order(models.Model):
    STATUS_CHOICES = [
        (1, 'در انتظار'),
        (2, 'پرداخت شده')
    ]

    buyer = models.ForeignKey(
        'accounts.Buyer',
        on_delete=models.CASCADE,
        verbose_name='خریدار'
    )

    products = models.ManyToManyField(
        'products.Product',
        verbose_name='محصول'
    )

    address = models.CharField(
        max_length=2000,
        verbose_name='آدرس'
    )

    phone_number = models.CharField(
        max_length=11,
        verbose_name='شماره تلفن'
    )

    delivery_date = models.DateField(
        verbose_name='زمان تحویل'
    )

    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=1,
        verbose_name='وضعیت'
    )

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش‌ها'

    def __str__(self):
        return str(self.id)

    @property
    def total_price(self):
        total_price = 0
        for product in self.products.all():
            total_price += product.price
        return total_price
