from django.views.generic import TemplateView
from .models import Hero
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
    
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

class HeroCreateView(CreateView):
    template_name = "add.html"
    model = Hero
    fields = '__all__'


class HeroUpdateView(UpdateView):
    template_name = "edit.html"
    model = Hero
    fields = '__all__'


class HeroDeleteView(DeleteView):
    model = Hero
    template_name = 'delete.html'
    success_url = reverse_lazy('hero_list')
