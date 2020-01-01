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

    class Meta:
        verbose_name = 'فروشنده'
        verbose_name_plural = 'فروشندگان'

    def __str__(self):
        return self.name
