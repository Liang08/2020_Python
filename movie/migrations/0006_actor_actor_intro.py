# Generated by Django 3.1.1 on 2020-09-09 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20200909_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='actor_intro',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
