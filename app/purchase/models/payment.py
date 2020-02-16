from datetime import datetime

from django.db import models, transaction


class Payment(models.Model):

    buyer = models.ForeignKey(
        'accounts.Buyer',
        on_delete=models.CASCADE,
        verbose_name='خریدار'
    )

    order = models.OneToOneField(
        'purchase.Order',
        on_delete=models.CASCADE,
        verbose_name='سفارش'
    )

    total_price = models.IntegerField(
        verbose_name='مبلغ'
    )

    payment_time = models.DateTimeField(
        default=datetime.now,
        verbose_name='زمان پرداخت'
    )

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        buyer = self.buyer
        buyer.credit -= self.total_price
        with transaction.atomic():
            buyer.save()
            super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'پرداخت'
        verbose_name_plural = 'پرداخت‌ها'
