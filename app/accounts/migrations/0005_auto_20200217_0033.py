# Generated by Django 2.2.8 on 2020-02-17 00:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_charge'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='commission',
            field=models.FloatField(default=0.2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)], verbose_name='مقدار کمیسیون'),
        ),
    ]
