import json

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient

from accounts.models import Vendor, Buyer, Charge
from purchase.models import Cart


class AccountAPITestCase(TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)

    def setUp(self):
        self.user1 = User.objects.create(username='user_1')
        self.user1.set_password('1234')
        self.user1.save()
        self.user2 = User.objects.create(username='user_2')
        self.user2.set_password('1234')
        self.user2.save()
        Vendor.objects.create(user=self.user1, name='vendor_1')
        cart = Cart.objects.create()
        Buyer.objects.create(user=self.user2, name='buyer_1', cart=cart)

    def test_api_authentication(self):
        response = self.client.post('/accounts/token/',
                                    {'username': 'user_1', 'password': '1234'},
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('access' in response.data)

        response = self.client.post('/accounts/token/',
                                    {'username': 'user_2', 'password': '1234'},
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('access' in response.data)

    def test_buyer_registration(self):
        response = self.client.post('/accounts/buyer-registration/',
                                    {'email': 'ali@ali.com', 'password': '1234', 'name': 'ali'},
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_vendor_registration(self):
        response = self.client.post('/accounts/vendor-registration/',
                                    {'email': 'reza@reza.com', 'password': '1234', 'name': 'reza'},
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_getting_user_type(self):
        response = self.client.post('/accounts/token/',
                                    {'username': self.user1.username, 'password': '1234'},
                                    content_type='application/json')

        token = response.data['access']
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = client.get('/accounts/get-type/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('type'), 'vendor')

    def test_charging(self):
        response = self.client.post('/accounts/token/',
                                    {'username': self.user2.username, 'password': '1234'},
                                    content_type='application/json')

        token = response.data['access']
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        data = {
            'user': self.user2.id,
            'amount': 12000
        }
        response = client.post('/accounts/charge/',
                               json.dumps(data),
                               content_type='application/json')
        self.assertEqual(response.status_code, 201)
        user_id = response.data.get('user')
        user = User.objects.get(id=user_id)
        credit = user.buyer.credit
        self.assertEqual(credit, 12000)

    def test_listing_transactions(self):
        response = self.client.post('/accounts/token/',
                                    {'username': self.user2.username, 'password': '1234'},
                                    content_type='application/json')

        token = response.data['access']
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        response = client.get('/accounts/charge/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)
