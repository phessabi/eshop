from django.contrib.auth.models import User
from django.test import TestCase

from accounts.models import Vendor, Buyer
from purchase.models import Cart


class AccountAPITestCase(TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)

    def setUp(self):
        user1 = User.objects.create(username='user_1')
        user1.set_password('1234')
        user1.save()
        user2 = User.objects.create(username='user_2')
        user2.set_password('1234')
        user2.save()
        Vendor.objects.create(user=user1, name='vendor_1')
        cart = Cart.objects.create()
        Buyer.objects.create(user=user2, name='buyer_1', cart=cart)

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
