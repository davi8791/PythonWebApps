from django.core.management.base import BaseCommand
from pathlib import Path
from csv import reader
from hero.models import Hero, Investigator


class Command(BaseCommand):
    def handle(self, *args, **options):
        load_data()


def load_data():
    Hero.objects.all().delete()
    path = Path('hero_objects.csv')
    with open(path) as f:
        file_reader = reader(f)
        for i in file_reader:
            Hero.objects.get_or_create(
                investigator=Investigator.objects.filter(pk=int(i[0]))[0],
                hero_name=i[1], 
                real_name=i[2], 
                about_1=i[3], 
                about_2=i[4], 
                about_source=i[5], 
                quote=i[6], 
                primary_rgb=i[7], 
                strengths=i[8], 
                weaknesses=i[9], 
                image=i[10], 
                )
    
