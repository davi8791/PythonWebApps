from pathlib import Path
from django.views.generic import TemplateView
import json

# I do something a little weird here
# This makes it so, in order to add a new superhero, the user only has to add an image and a json file to the static/images directory
# The json is necessary to provide data that cannot all be contained in an image file
def retrieve_heroes():
    path = list(Path('static/images').iterdir())
    heroes = []
    for f in path:
        if f.suffix == ".json":
            file_contents = f.read_text()
            file_data = json.loads(file_contents)
            for nf in path:
                if nf.suffix != ".json" and nf.with_suffix("") == f.with_suffix(""):
                    file_data["file"] = nf
            heroes.append(file_data)
    return heroes
    
class HeroListView(TemplateView):
    template_name = 'heroes.html'
    def get_context_data(self, **kwargs):
        return dict(hero=retrieve_heroes())

class HeroDetailView(TemplateView):
    template_name = 'hero.html'
    def get_context_data(self, **kwargs):
        heroes = retrieve_heroes()
        for i in heroes:
            if i["hero_name"] == kwargs['hero_name']:
                return dict(hero=i)
        return dict()

        
