from json import dump
from django.core.management.base import BaseCommand
from hero.models import Hero


class Command(BaseCommand):

    def handle(self, *args, **options):
        save_data()


def save_data():
    data = [b for b in Hero.objects.all().values()]

    with open('hero_objects.json', "w") as f:
        dump(data, f, indent=4)