from core import models

from django.contrib import admin

# Register your models here.
admin.site.register(models.Author)
admin.site.register(models.Book)
admin.site.register(models.Character)
admin.site.register(models.CharacterRace)
