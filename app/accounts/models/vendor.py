from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Vendor(models.Model):
    user = models.OneToOneField(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name='کاربر'
    )

    name = models.CharField(
        max_length=100,
        verbose_name='نام'
    )

    logo = models.ImageField(
        upload_to='resources/images/vendors',
        null=True,
        blank=True,
        verbose_name='لوگو'
    )

    credit = models.IntegerField(
        default=0,
        verbose_name='اعتبار'
    )

    commission = models.FloatField(
        validators=(MinValueValidator(0), MaxValueValidator(1)),
        default=0.2,
        verbose_name='مقدار کمیسیون'
    )

    active = models.BooleanField(
        default=True,
        verbose_name='فعال'
    )

    def save(self, *args, **kwargs):
        old_object = Vendor.objects.get(id=self.id) if self.id else None

        if old_object:
            if not old_object.active and self.credit > 0:
                self.active = True
            elif old_object.active and self.credit < 0:
                self.active = False
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'فروشنده'
        verbose_name_plural = 'فروشندگان'
