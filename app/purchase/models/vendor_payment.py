from django.db import models

from accounts.models import Vendor, Buyer
from products.models import Product


class VendorPayment(models.Model):
    vendor = models.OneToOneField(
        to=Vendor,
        on_delete=models.CASCADE,
        verbose_name='فروشنده'
    )

    buyer = models.OneToOneField(
        to=Buyer,
        on_delete=models.CASCADE,
        verbose_name='خریدار',
    )

    product = models.OneToOneField(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name='محصول',
    )

    amount = models.PositiveIntegerField(
        verbose_name='مبلغ پرداخت',
    )

    def save(self, *args, **kwargs):
        system_share = self.vendor.commission * self.amount
        self.vendor.credit -= system_share
        self.vendor.save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'پرداخت فروشنده'
        verbose_name_plural = 'پرداخت‌های فروشندگان'
