from pathlib import Path
from django.views.generic import TemplateView
from .models import Hero
    
class HeroListView(TemplateView):
    template_name = 'heroes.html'
    def get_context_data(self, **kwargs):
        return {
            "heroes": Hero.objects.all()
        }

class HeroDetailView(TemplateView):
    template_name = 'hero.html'
    def get_context_data(self, **kwargs):
        return {
            "hero": Hero.objects.get(pk=kwargs['pk'])
        }

        
