# Generated by Django 2.2.8 on 2020-01-13 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='archived',
            field=models.BooleanField(default=False, verbose_name='حذف شده'),
        ),
    ]