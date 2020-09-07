from django.test import TestCase

from google_books_api.BookFinder import BookFinder

from requests import codes

import responses

URI = "https://www.googleapis.com/books/v1/volumes"
TITLE = "Guards! Guards!"
AUTHOR = "Terry Pratchett"
ISBN = "1407034693"


class BookFinderTests(TestCase):

    @responses.activate
    def test_BookFinder_full_criteria(self):
        responses.add(responses.GET, "https://www.googleapis.com/books/v1/volumes?q=intitle%3AGuards%21+Guards%21%2Binauthor%3ATerry+Pratchett%2Bisbn%3A1407034693", status=codes.OK)

        bookFinder = BookFinder(URI)
        bookFinder.set_title(TITLE)
        bookFinder.set_author(AUTHOR)
        bookFinder.set_isbn(ISBN)

        status_code = bookFinder.find_a_book()

        self.assertTrue(status_code, codes.ok)
        self.assertEqual(bookFinder.get_status_code(), codes.ok)

    @responses.activate
    def test_BookFinder_only_title(self):
        responses.add(responses.GET, "https://www.googleapis.com/books/v1/volumes?q=intitle%3AGuards%21+Guards%21", status=codes.OK)

        bookFinder = BookFinder(URI)
        bookFinder.set_title(TITLE)

        status_code = bookFinder.find_a_book()

        self.assertTrue(status_code, codes.ok)
        self.assertEqual(bookFinder.get_status_code(), codes.ok)

    @responses.activate
    def test_BookFinder_only_author(self):
        responses.add(responses.GET, "https://www.googleapis.com/books/v1/volumes?q=inauthor%3ATerry+Pratchett", status=codes.OK)

        bookFinder = BookFinder(URI)
        bookFinder.set_author(AUTHOR)

        status_code = bookFinder.find_a_book()

        self.assertTrue(status_code, codes.ok)
        self.assertEqual(bookFinder.get_status_code(), codes.ok)

    @responses.activate
    def test_BookFinder_only_isbn(self):
        responses.add(responses.GET, "https://www.googleapis.com/books/v1/volumes?q=isbn%3A1407034693", status=codes.OK)

        bookFinder = BookFinder(URI)
        bookFinder.set_isbn(ISBN)

        status_code = bookFinder.find_a_book()

        self.assertTrue(status_code, codes.ok)
        self.assertEqual(bookFinder.get_status_code(), codes.ok)

    @responses.activate
    def test_BookFinder_author_and_isbn(self):
        responses.add(responses.GET, "https://www.googleapis.com/books/v1/volumes?q=inauthor%3ATerry+Pratchett%2Bisbn%3A1407034693", status=codes.OK)

        bookFinder = BookFinder(URI)
        bookFinder.set_author(AUTHOR)
        bookFinder.set_isbn(ISBN)

        status_code = bookFinder.find_a_book()

        self.assertTrue(status_code, codes.ok)
        self.assertEqual(bookFinder.get_status_code(), codes.ok)
