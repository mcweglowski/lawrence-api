from book.serializers import BookSerializer
from book.views import BookViewSet

import collections

from core.models import Book

from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory


class BookViewSetTests(TestCase):

    def setUp(self):
        self.book = Book()
        self.book.title = "some_book"
        self.book.publishing_year = 2000
        self.book.isbn = "123456"
        self.book.save()

    def test_get(self):
        response = self.client.get(f'/api/book/books/',
                                   {'pk': self.book.pk},
                                   follow=True)

        serializer = BookSerializer(self.book, many=False)
        expected = [collections.OrderedDict(serializer.data)]
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, expected)

    def test_basic_view_get(self):
        response = self.client.get(f'/api/book/books/',
                                   {'title': 'some_book'},
                                   follow=True)

        serializer = BookSerializer(self.book, many=False)
        expected = [collections.OrderedDict(serializer.data)]
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, expected)
