from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

HELLO_WORLD_URL = '/api/hello-world/'


class HelloWorldTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_hello_world_function_based_view(self):
        expected = {"message": "Hello World!"}

        res = self.client.get(HELLO_WORLD_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, expected)
