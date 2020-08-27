from django.db import models


class Author(models.Model):
    first_name      = models.CharField(max_length=255, null=True)
    last_name       = models.CharField(max_length=255, null=True)
    display_name    = models.CharField(max_length=255, null=True)
    date_of_birth   = models.DateField(null=True)
    date_of_death   = models.DateField(null=True)

    def __str__(self):
        if self.display_name is None:
            return f"{self.first_name} {self.last_name}"
        return self.display_name