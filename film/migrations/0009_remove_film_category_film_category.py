# Generated by Django 5.1.1 on 2024-10-18 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0008_film_favourites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='category',
        ),
        migrations.AddField(
            model_name='film',
            name='category',
            field=models.ManyToManyField(blank=True, to='film.category'),
        ),
    ]
