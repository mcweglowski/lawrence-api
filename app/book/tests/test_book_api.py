from book.serializers import BookSerializer

from core.models import Book

from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient


BOOK_URL = "/api/book/books/"


def detail_url(id):
    return f"{BOOK_URL}{id}/"


def sample_Book(title, publishing_year, isbn):
    return Book.objects.create(
        title=title,
        publishing_year=publishing_year,
        isbn=isbn
    )


class BookAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.book1 = sample_Book("Book1", 2020, 123)
        self.book2 = sample_Book("Book2", 2019, 456)
        self.book3 = sample_Book("Book3", 2018, 789)

    def test_retrieve_all_books(self):

        res = self.client.get(BOOK_URL)

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_retrieve_one_book(self):

        res = self.client.get(detail_url(self.book1.id))

        serializer = BookSerializer(self.book1, many=False)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
