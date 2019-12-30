from django.db import models


class Category(models.Model):
    STAGE_CHOICES = [
        (1, 'سطح اول'),
        (2, 'سطح دوم'),
        (3, 'سطح سوم'),
    ]
    name = models.CharField(max_length=50,
                            verbose_name='نام')
    stage = models.IntegerField(choices=STAGE_CHOICES,
                                verbose_name='سطح')
    parent_category = models.ForeignKey('self',
                                        on_delete=models.CASCADE,
                                        verbose_name='دسته پدر')

    class Meta:
        verbose_name = 'دسته'
        verbose_name_plural = 'دسته‌ها'
