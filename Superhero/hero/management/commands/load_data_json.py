from django.core.management.base import BaseCommand
from json import loads
from pathlib import Path

from hero.models import Hero


class Command(BaseCommand):
    def handle(self, *args, **options):
        load_data()


def load_data():
    # Delete the old objects
    Hero.objects.all().delete()

    # Read the JSON file
    path = Path('hero_objects.json')
    if path.exists():
        objects = loads(path.read_text())

    # Create new objects
    for o in objects:
        Hero.objects.get_or_create(**o)

    # Show the objects
    for hero in Hero.objects.all().values():
        print(hero)
