from csv import writer
from django.core.management.base import BaseCommand
from hero.models import Hero


class Command(BaseCommand):

    def handle(self, *args, **options):
        save_data()


def save_data():
    data = [
        [
            hero.investigator.pk,
            hero.hero_name, 
            hero.real_name, 
            hero.about_1, 
            hero.about_2, 
            hero.about_source, 
            hero.quote,
            hero.primary_rgb,
            hero.strengths,
            hero.weaknesses,
            hero.image.pk
        ] for hero in Hero.objects.all()]

    with open('hero_objects.csv', 'w', newline='') as f:
        writer(f).writerows(data)
