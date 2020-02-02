# Generated by Django 2.2.8 on 2020-01-01 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('level', models.IntegerField(choices=[(1, 'سطح اول'), (2, 'سطح دوم'), (3, 'سطح سوم')], verbose_name='سطح')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Category', verbose_name='دسته پدر')),
            ],
            options={
                'verbose_name': 'دسته',
                'verbose_name_plural': 'دسته\u200cها',
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='نام')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category', verbose_name='دسته')),
            ],
            options={
                'verbose_name': 'فیلد',
                'verbose_name_plural': 'فیلدها',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='عنوان')),
                ('image', models.ImageField(blank=True, null=True, upload_to='resources/images/products', verbose_name='تصویر')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('express', models.BooleanField(default=False, verbose_name='فوری')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category', verbose_name='دسته')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Vendor', verbose_name='فروشنده')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1024, verbose_name='مقدار')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Field', verbose_name='فیلد')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'مشخصات محصول',
                'verbose_name_plural': 'مشخصات محصولات',
            },
        ),
        migrations.AddConstraint(
            model_name='field',
            constraint=models.UniqueConstraint(fields=('name', 'category'), name='unique_field'),
        ),
    ]