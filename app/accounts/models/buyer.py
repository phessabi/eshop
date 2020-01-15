from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Buyer(models.Model):
    user = models.OneToOneField(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name='کاربر'
    )

    name = models.CharField(
        max_length=100,
        verbose_name='نام'
    )

    address = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name='آدرس'
    )

    phone_number = PhoneNumberField(
        null=True,
        blank=True,
        verbose_name='شماره تلفن'
    )

    credit = models.IntegerField(
        default=0,
        verbose_name='اعتبار'
    )

    class Meta:
        verbose_name = 'خریدار'
        verbose_name_plural = 'خریداران'

    def __str__(self):
        return self.name
