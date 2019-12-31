from django.db import models


class Category(models.Model):
    LEVEL_CHOICES = [
        (1, 'سطح اول'),
        (2, 'سطح دوم'),
        (3, 'سطح سوم'),
    ]

    name = models.CharField(
        max_length=50,
        verbose_name='نام'
    )

    level = models.IntegerField(
        choices=LEVEL_CHOICES,
        verbose_name='سطح'
    )

    parent_category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='دسته پدر'
    )

    class Meta:
        verbose_name = 'دسته'
        verbose_name_plural = 'دسته‌ها'

    def __str__(self):
        return self.name
