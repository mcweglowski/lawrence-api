from core import models

from django.test import TestCase


class ModelTests(TestCase):

    def test_author_str_when_no_display_name_provided(self):
        first_name = "John"
        last_name = "Tolkien"

        author = models.Author.objects.create(
            first_name=first_name,
            last_name=last_name)

        self.assertEqual(str(author), f"{first_name} {last_name}")

    def test_author_str_when_display_name_provided(self):
        first_name = "John"
        last_name = "Tolkien"
        display_name = "John R. R. Tolkien"

        author = models.Author.objects.create(
            first_name=first_name,
            last_name=last_name,
            display_name=display_name)

        self.assertEqual(str(author), display_name)

    def test_book_str_when_no_year_provided(self):
        title = "The Lord of the Rings"

        book = models.Book.objects.create(
            title=title,
            isbn=0
        )

        self.assertEqual(str(book), title)

    def test_book_str_when_year_provided(self):
        title = "The Lord of the Rings"
        publishing_year = 1954

        book = models.Book.objects.create(
            title=title,
            publishing_year=publishing_year,
            isbn=0
        )

        self.assertEqual(str(book), f"{title}({publishing_year})")
