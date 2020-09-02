from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    display_name = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(null=True)
    date_of_death = models.DateField(null=True)

    def __str__(self):
        if self.display_name:
            return self.display_name
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    publishing_year = models.PositiveSmallIntegerField(null=True)
    isbn = models.PositiveBigIntegerField(default=None)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        if self.publishing_year:
            return f"{self.title}({self.publishing_year})"
        return self.title
