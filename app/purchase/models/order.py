from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    PENDING = 1
    PAID = 2

    STATUS_CHOICES = [
        (PENDING, 'در انتظار'),
        (PAID, 'پرداخت شده')
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

    phone_number = PhoneNumberField(
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

    @property
    def total_price(self):
        total_price = 0
        for product in self.products.all():
            total_price += product.price
        return total_price

    @property
    def total_price_after_sale(self):
        total_price = 0
        for product in self.products.all():
            total_price += product.price_after_sale
        return total_price

    def affect_commission(self):
        for product in self.products.all():
            vendor = product.vendor
            price = product.price_after_sale
            system_share = price * vendor.commission
            vendor.credit -= system_share
            vendor.save()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش‌ها'
