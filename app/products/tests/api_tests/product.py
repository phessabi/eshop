from django.contrib.auth.models import User
from django.test import TestCase

from accounts.models import Vendor
from products.models import Category, Product


class ProductAPITestCase(TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.category_id = None
        self.vendor_id = None

    def setUp(self):
        user = User.objects.create(username='user_1')
        user.set_password('1234')
        user.save()
        vendor = Vendor.objects.create(user=user, name='vendor_1')
        category = Category.objects.create(name='cat_1', level=1)
        Product.objects.create(title='product_1', category=category, price=500, vendor=vendor)
        Product.objects.create(title='product_2', category=category, price=500, vendor=vendor)
        Product.objects.create(title='product_3', category=category, price=500, vendor=vendor)

        self.category_id = category.id
        self.vendor_id = vendor.id

    # def test_api_authentication(self):
    #     data = {
    #         'title': 'new_prod',
    #         'category': self.category_id,
    #         'price': 100,
    #         'vendor': self.vendor_id
    #     }
    #     response = self.client.post('http://0.0.0.0:8000/products/vendor-product/', data, content_type='application/json')
    #
    #     self.assertEqual(response.status_code, 201)

    # def test_product_post(self):
    #     data = {
    #         'title': 'new_prod',
    #         'category': self.category_id,
    #         'price': 100,
    #         'vendor': self.vendor_id
    #     }
    #     self.client.login(username='user_1', password='1234')
    #     response = self.client.post('http://0.0.0.0:8000/products/vendor-product/', data, content_type='application/json')
    #     content = response.json()
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(Product.objects.count(), 4)
    #
    #     category_id = content['category']
    #     category = Category.objects.get(id=category_id)
    #
    #     vendor_id = content['vendor']
    #     vendor = Vendor.objects.get(id=vendor_id)
    #
    #     self.assertEqual(vendor.product_set.count(), 4)
    #     self.assertEqual(category.product_set.count(), 4)
    #     self.assertEqual(content['title'], 'new_prod')
    #     self.assertEqual(content['price'], 100)

    # def test_product_list(self):
    #     self.client.login(username='user_1', password='1234')
    #     response = self.client.get('http://0.0.0.0:8000/products/vendor-product/')
    #     content = response.json()
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(content), 3)
    #     for i in range(3):
    #         product_detail = content[i]
    #         self.assertEqual(product_detail['price'], 500)
    #         self.assertEqual(product_detail['title'], f'product_{i + 1}')

    def test_category_list(self):
        response = self.client.get('http://0.0.0.0:8000/products/list-categories/')
        content = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(content), 1)

    def test_product_list(self):
        response = self.client.get('http://0.0.0.0:8000/products/list-products/')
        content = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(content), 3)
