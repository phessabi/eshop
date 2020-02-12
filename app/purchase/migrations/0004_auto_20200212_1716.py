# Generated by Django 2.2.8 on 2020-02-12 17:16

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0003_auto_20200208_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='شماره تلفن'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='purchase.Order', verbose_name='سفارش'),
        ),
    ]
