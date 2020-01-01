from django.contrib.auth.models import User
from django.test import TestCase

from accounts.models import Vendor
from products.models import Product, Category


class ProductModelTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='user_1')
        vendor = Vendor.objects.create(user=user, name='vendor_1')
        category = Category.objects.create(name='cat_1', level=1)
        Product.objects.create(title='product_1', category=category, price=500, vendor=vendor)
        Product.objects.create(title='product_2', category=category, price=500, vendor=vendor)
        Product.objects.create(title='product_3', category=category, price=500, vendor=vendor)

    def test_product_database(self):
        self.assertEqual(Product.objects.count(), 3)
