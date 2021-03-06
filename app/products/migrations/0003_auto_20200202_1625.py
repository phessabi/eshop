# Generated by Django 2.2.8 on 2020-02-02 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_archived'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='field',
            name='unique_field',
        ),
        migrations.AlterField(
            model_name='field',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='products.Category', verbose_name='دسته'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specifications', to='products.Product', verbose_name='محصول'),
        ),
        migrations.AlterUniqueTogether(
            name='field',
            unique_together={('name', 'category')},
        ),
    ]
