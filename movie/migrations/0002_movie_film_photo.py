# Generated by Django 3.1.1 on 2020-09-09 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='film_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
