import json

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient

from accounts.models import Vendor
from products.models import Category, Product


class CategoryAPITestCase(TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.admin = None

    def setUp(self):
        self.admin = User.objects.create_superuser(username='user_1', email='user@user.com', password='1234')

    def test_category_creation(self):
        response = self.client.post('/accounts/token/',
                                    {'username': self.admin.username, 'password': '1234'},
                                    content_type='application/json')
        token = response.data['access']
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        data = {
            'name': 'cat_1',
            'level': 1,
        }
        response = client.post('/products/admin-category/',
                               json.dumps(data),
                               content_type='application/json')

        self.assertEqual(response.status_code, 201)

        data = {
            'name': 'cat_2',
            'level': 2
        }

        response = client.post('/products/admin-category/',
                               json.dumps(data),
                               content_type='application/json')

        self.assertEqual(response.status_code, 400)
