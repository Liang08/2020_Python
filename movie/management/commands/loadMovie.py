from pathlib import Path
from json import load

from django.core.management.base import BaseCommand
from django.db import transaction

from movie.models import Actor, Movie, Comment


class Command(BaseCommand):
    help = "Load actors from directory's json files"

    def add_arguments(self, parser):
        parser.add_argument('directory', type=Path)

    def handle(self, *args, **options):
        directory = options['directory']
        for path in directory.iterdir():
            data = load(open(str(path), encoding='utf-8'))
            actors = data.pop('actor')
            comments = data.pop('commit')
            movie = Movie.objects.create(**data)
            for a in actors:
                info = Actor.objects.filter(actor_name=a)
                if info.exists():
                    movie.actor.add(Actor.objects.filter(actor_name=a)[0])
            for a in comments:
                movie.comment_set.create(comment=a)
