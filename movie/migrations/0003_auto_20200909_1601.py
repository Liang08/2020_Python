# Generated by Django 3.1.1 on 2020-09-09 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movie_film_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='film_photo',
        ),
        migrations.AddField(
            model_name='actor',
            name='actor_number',
            field=models.IntegerField(default=0),
        ),
    ]
