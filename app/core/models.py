from django.db import models


class CharacterRace(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Character(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    race = models.ForeignKey(CharacterRace, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"


class Author(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    display_name = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        if self.display_name:
            return self.display_name
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    publishing_year = models.PositiveSmallIntegerField(null=True)
    isbn = models.CharField(max_length=13)
    authors = models.ManyToManyField(Author)
    characters = models.ManyToManyField(Character)

    def __str__(self):
        if self.publishing_year:
            return f"{self.title}({self.publishing_year})"
        return self.title
