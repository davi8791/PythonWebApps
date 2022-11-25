from .models import Hero
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Hero, Investigator
from csv import reader
from markdown import markdown
from os.path import exists


def list_heroes(investigator):
    return dict(heroes=Hero.objects.filter(investigator=investigator))

def get_investigator(user):
    return Investigator.objects.get_or_create(user=user)[0]

def lorem(num_words):
    text = open('Documents/lorem.txt').read()
    text = ' '.join(text.split(' ')[: num_words])
    return f'#### Lorem {num_words}\n\n' + text

def card_data(title="Random Card", body=None, color='bg-primary text-light', width='col-lg-12', link=None):
    if not body:
        body = lorem(400)
    html = markdown(body)
    return dict(title=title, header=title, body=html, color=color, width=width)

def cards_data():
    return [
        card_data(),
        card_data("Card Two",   lorem(50),  "bg-warning text-dark", 'col-lg-6'),
        card_data("Card Three", lorem(150), "bg-success text-light", 'col-lg-6'),
        card_data("Card Four",  lorem(20),  "bg-danger text-light",  'col-lg-6'),
    ]

def tabs_data():

    def options(i, tab, selected):
        data = tab
        if selected:
            data.update(dict(name=f'tab{i}', active='active', show='show', selected='true'))
        else:
            data.update(dict(name=f'tab{i}', active='', show='', selected='false'))
        return data

    def set_options(tabs):
        return [options(i, tab, i == 0) for i, tab in enumerate(tabs)]

    def create_pane_1():
        data = card_data(title="Investigator", body='Investigator')
        data['cards'] = cards_data()
        return data

    def create_pane_2():
        data = card_data(title="My Superheroes", body='My Superheroes')
        data['cards'] = cards_data()
        return data

    def create_tabs():
        return [
            create_pane_1(),
            create_pane_2(),
        ]

    return set_options(create_tabs())


class InvestigatorHomeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return '/hero/'
        return f'/investigator/{get_investigator(self.request.user).pk}'

class InvestigatorDetailView(DetailView):
    template_name = 'investigator/detail.html'
    model = Investigator

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        tabs = [
            dict(name='investigator-tab', header='Investigator', title=False, investigator=True, active='active', show='show', selected='true'), 
            dict(name='heroes-tab', header='My Heroes', title=False, heroes=True, active='', show='', selected='false')
            ]
        kwargs.update(list_heroes(kwargs.get('object')))
        kwargs.update(tabs=tabs)
        return kwargs

class InvestigatorAddView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/account_add.html'
    success_url = reverse_lazy('investigator_home')

class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "registration/account_edit.html"
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    success_url = reverse_lazy('investigator_home')

class InvestigatorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "investigator/edit.html"
    model = Investigator
    fields = '__all__'
    success_url = reverse_lazy('investigator_home')

class InvestigatorDeleteView(LoginRequiredMixin, DeleteView):
    model = Investigator
    template_name = 'investigator/delete.html'
    success_url = reverse_lazy('heroes')

class HeroListView(ListView):
    template_name = "hero/list.html"
    model = Hero
    fields = '__all__'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs.update(dict(heroes=Hero.objects.all()))
        return kwargs

class HeroDetailView(DetailView):
    template_name = "hero/detail.html"
    model = Hero
    fields = '__all__'
    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs.update(dict(cards=[
            dict(title='Strengths', body=kwargs['hero'].strengths, width='400', color='bg-success text-light'),
            dict(title='Weaknesses', body=kwargs['hero'].weaknesses, width='400', color='bg-danger text-light')
            ]))
        return kwargs

class HeroCreateView(LoginRequiredMixin, CreateView):
    template_name = "hero/add.html"
    model = Hero
    fields = '__all__'
    success_url = reverse_lazy('investigator_home')

    def form_valid(self, form):
        form.instance.investigator = get_investigator(self.request.user)
        return super().form_valid(form)

class HeroUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "hero/edit.html"
    model = Hero
    fields = '__all__'
    success_url = reverse_lazy('investigator_home')

class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Hero
    template_name = 'hero/delete.html'
    success_url = reverse_lazy('investigator_home')

class TabsView(TemplateView):
    template_name = 'tabs.html'

    def get_context_data(self, **kwargs):
        tabs = tabs_data()
        return dict(title='Tab View', tabs=tabs)
