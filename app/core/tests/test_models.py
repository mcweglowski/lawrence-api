from core import models

from django.test import TestCase


class ModelTests(TestCase):

    def test_author_str_when_no_display_name_provided(self):
        first_name = "John"
        last_name = "Tolkien"

        author = models.Author.objects.create(
            first_name = first_name,
            last_name = last_name
        )

        self.assertEqual(str(author), f"{first_name} {last_name}")

    def test_author_str_when_display_name_provided(self):
        first_name = "John"
        last_name = "Tolkien"
        display_name = "John R. R. Tolkien"

        author = models.Author.objects.create(
            first_name = first_name,
            last_name = last_name,
            display_name = display_name
        )

        self.assertEqual(str(author), display_name)
