from django.db import models


class Field(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='نام'
    )

    category = models.ForeignKey(
        'products.Category',
        on_delete=models.CASCADE,
        related_name='fields',
        verbose_name='دسته'
    )

    class Meta:
        verbose_name = 'فیلد'
        verbose_name_plural = 'فیلدها'
        unique_together = ['name', 'category']

    def __str__(self):
        return self.name
