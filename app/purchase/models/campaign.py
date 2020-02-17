from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from accounts.models import Vendor


class Campaign(models.Model):
    vendor = models.OneToOneField(
        to=Vendor,
        on_delete=models.CASCADE,
        verbose_name='فروشنده'
    )

    start_datetime = models.DateField(
        verbose_name='زمان شروع'
    )

    end_datetime = models.DateField(
        verbose_name='زمان پایان'
    )

    sale_amount = models.FloatField(
        validators=(MinValueValidator(0), MaxValueValidator(1)),
        verbose_name='مقدار تخفیف'
    )

    class Meta:
        verbose_name = 'کمپین'
        verbose_name_plural = 'کمپین‌ها'
