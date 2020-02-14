from django.contrib.auth.models import User
from django.test import TestCase

from accounts.models import Vendor
from products.models import Product, Category
from products.views.public_views.product import list_all_products


class ProductModelTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='user_1')
        vendor = Vendor.objects.create(user=user, name='vendor_1')
        self.category1 = Category.objects.create(name='cat_1', level=1)
        self.category2 = Category.objects.create(name='cat_2', level=2, parent_category=self.category1)
        self.category3 = Category.objects.create(name='cat_3', level=3, parent_category=self.category2)
        self.category4 = Category.objects.create(name='cat_3', level=1)
        Product.objects.create(title='product_1', category=self.category3, price=500, vendor=vendor)
        Product.objects.create(title='product_2', category=self.category3, price=500, vendor=vendor)
        Product.objects.create(title='product_3', category=self.category4, price=500, vendor=vendor)

    def test_product_database(self):
        self.assertEqual(Product.objects.count(), 3)

    def test_listing_subcategories(self):
        self.assertEqual(len(list_all_products(self.category1)), 2)
