# Generated by Django 3.1 on 2020-08-27 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='author',
            name='date_of_death',
        ),
        migrations.RemoveField(
            model_name='author',
            name='display_name',
        ),
    ]
