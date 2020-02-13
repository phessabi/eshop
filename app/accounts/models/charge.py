from datetime import datetime

from django.db import models


class Charge(models.Model):

    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name='کاربر'
    )

    amount = models.IntegerField(
        verbose_name='هزینه'
    )

    payment_time = models.DateTimeField(
        default=datetime.now,
        verbose_name='زمان پرداخت'
    )

    class Meta:
        verbose_name = 'شارژ حساب'
        verbose_name_plural = 'شارژهای حساب'

    def __str__(self):
        return str(self.id)
