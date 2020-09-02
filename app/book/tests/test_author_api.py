from datetime import date
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from book.serializers import AuthorSerializer
from core.models import Author


AUTHOR_URL = "/api/author/"


def detail_url(id):
    return f"{AUTHOR_URL}{id}/"


def sample_author1():
    return Author.objects.create(
        first_name="Terry",
        last_name="Pratchett",
        date_of_birth=date(1948, 4, 28),
        date_of_death=date(2015, 3, 12))


def sample_author2():
    return Author.objects.create(
        first_name="Ziemowit",
        last_name="Szczerek",
        date_of_birth=date(1978, 4, 10))


def sample_author3():
    return Author.objects.create(
        first_name="George",
        last_name="Martin",
        date_of_birth=date(1948, 9, 22))


class AuthorAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.author1 = sample_author1()
        self.author2 = sample_author2()
        self.author3 = sample_author3()

    def test_retrieve_all_authors(self):

        res = self.client.get(AUTHOR_URL)

        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_retrieve_one_author(self):

        res = self.client.get(detail_url(self.author2.id))

        serializer = AuthorSerializer(self.author2)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
