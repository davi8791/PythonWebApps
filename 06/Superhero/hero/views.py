from .models import Hero
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

class HeroListView(ListView):
    template_name = "heroes.html"
    model = Hero
    fields = '__all__'

class HeroDetailView(DetailView):
    template_name = "hero.html"
    model = Hero
    fields = '__all__'

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
