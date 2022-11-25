from .models import Hero
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView
from .models import Hero, Investigator, Photo


def list_heroes(investigator):
    return dict(heroes=Hero.objects.filter(investigator=investigator))

def get_investigator(user):
    return Investigator.objects.get_or_create(user=user)[0]

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

class PhotoDetailView(DetailView):
    template_name = 'photo/detail.html'
    model = Photo
    context_object_name = 'photo'

class PhotoCreateView(CreateView):
    template_name = 'photo/add.html'
    model = Photo
    fields = '__all__'

class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Hero
    template_name = 'hero/delete.html'
    success_url = reverse_lazy('investigator_home')

class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'photo/edit.html'
    model = Photo
    fields = '__all__'

class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'photo/delete.html'
    model = Photo
    success_url = reverse_lazy('photos')

class PhotoListView(ListView):
    template_name = 'photo/photos.html'
    model = Photo

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        photos = Photo.objects.all()
        photos_list = []
        first = True
        for i in photos:
            if first:
                photos_list.append(dict(image_url=i.image_url, pk=i.pk, label=i.title, active='active'))
                first = False
            else:
                photos_list.append(dict(image_url=i.image_url, pk=i.pk, label=i.title, active=''))

        kwargs.update(carousel=photos_list)
        return kwargs
