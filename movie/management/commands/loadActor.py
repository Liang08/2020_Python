from pathlib import Path
from json import load

from django.core.management.base import BaseCommand
from django.db import transaction

from movie.models import Actor


class Command(BaseCommand):
    help = "Load actors from directory's json files"

    def add_arguments(self, parser):
        parser.add_argument('directory', type=Path)

    def handle(self, *args, **options):
        directory = options['directory']
        actor = []
        for path in directory.iterdir():
            data = load(open(str(path), encoding='utf-8'))
            actor.append(Actor(**data))
        Actor.objects.bulk_create(actor)
