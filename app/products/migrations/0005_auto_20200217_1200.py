# Generated by Django 2.2.8 on 2020-02-17 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200217_1118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='price_before_sale',
        ),
    ]