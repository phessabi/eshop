import json

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient

from accounts.models import Buyer, Vendor
from products.models import Category, Product
from purchase.models import Cart, Order


class PurchaseAPITestCase(TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)

    def setUp(self):
        user1 = User.objects.create(username='user_1')
        user1.set_password('1234')
        user1.save()
        vendor = Vendor.objects.create(user=user1, name='vendor_1')
        user2 = User.objects.create(username='user_2')
        user2.set_password('1234')
        user2.save()
        cart = Cart.objects.create()
        self.buyer = Buyer.objects.create(user=user2, name='buyer_1', cart=cart)
        category = Category.objects.create(name='cat_1', level=1)
        self.product1 = Product.objects.create(title='product_1', category=category, price=500, vendor=vendor)
        self.product2 = Product.objects.create(title='product_2', category=category, price=500, vendor=vendor)
        self.product3 = Product.objects.create(title='product_3', category=category, price=500, vendor=vendor)

    def test_add_to_cart(self):
        response = self.client.post('/accounts/token/',
                                    {'username': self.buyer.user.username, 'password': '1234'},
                                    content_type='application/json')
        token = response.data['access']
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        data = {
            'id': self.product1.id
        }
        cart_id = self.buyer.cart.id
        response = client.put('/purchase/cart/' + str(cart_id) + '/',
                              json.dumps(data),
                              content_type='application/json')

        self.assertEqual(response.status_code, 200)

        response = client.get('/purchase/cart/')
        content = response.json()[0]
        products = content['products']
        self.assertEqual(len(products), 1)

    def test_delete_from_cart(self):
        response = self.client.post('/accounts/token/',
                                    {'username': self.buyer.user.username, 'password': '1234'},
                                    content_type='application/json')
        token = response.data['access']
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        data = {
            'id': self.product1.id
        }
        cart_id = self.buyer.cart.id
        response = client.put('/purchase/cart/' + str(cart_id) + '/',
                              json.dumps(data),
                              content_type='application/json')

        self.assertEqual(response.status_code, 200)

        response = client.get('/purchase/cart/')
        content = response.json()[0]
        products = content['products']
        self.assertEqual(len(products), 1)

        response = client.delete('/purchase/cart/' + str(cart_id) + '/',
                                 json.dumps(data),
                                 content_type='application/json')

        self.assertEqual(response.status_code, 204)

        response = client.get('/purchase/cart/')
        content = response.json()[0]
        products = content['products']
        self.assertEqual(len(products), 0)

    def test_order_completion(self):
        response = self.client.post('/accounts/token/',
                                    {'username': self.buyer.user.username, 'password': '1234'},
                                    content_type='application/json')
        token = response.data['access']
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        data = {
            'buyer': self.buyer.id,
            'products': [
                {
                    'id': self.product2.id
                }
            ],
            'address': 'a chert address',
            'phone_number': '+989308005234',
            'delivery_date': '2020-02-11'
        }
        response = client.post('/purchase/order/',
                               json.dumps(data),
                               content_type='application/json')

        self.assertEqual(response.status_code, 201)
        orders = Order.objects.all()
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0].status, 1)

    def test_payment(self):
        response = self.client.post('/accounts/token/',
                                    {'username': self.buyer.user.username, 'password': '1234'},
                                    content_type='application/json')
        token = response.data['access']
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        data = {
            'buyer': self.buyer.id,
            'products': [
                {
                    'id': self.product2.id
                }
            ],
            'address': 'a chert address',
            'phone_number': '+989308005234',
            'delivery_date': '2020-02-11'
        }
        response = client.post('/purchase/order/',
                               json.dumps(data),
                               content_type='application/json')

        order_id = response.data.get('id')
        order = Order.objects.get(id=order_id)
        data = {
            'order': order_id,
            'buyer': self.buyer.id,
            'total_price': order.total_price
        }
        response = client.post('/purchase/payment/',
                               json.dumps(data),
                               content_type='application/json')

        self.assertEqual(response.status_code, 201)

        response = client.get('/purchase/order/')
        self.assertEqual(len(response.data), 1)

        response = client.get('/purchase/payment/')
        self.assertEqual(len(response.data), 1)
