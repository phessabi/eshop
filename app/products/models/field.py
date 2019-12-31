from django.db import models


class Field(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='نام'
    )

    category = models.ForeignKey(
        'products.Category',
        on_delete=models.CASCADE,
        verbose_name='دسته'
    )

    class Meta:
        verbose_name = 'فیلد'
        verbose_name_plural = 'فیلدها'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'category'],
                name='unique_field'
            )
        ]

    def __str__(self):
        return self.name
