from .models import Hero
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Hero, Author, Message


def list_heroes(author):
    return dict(heroes=Hero.objects.filter(author=author))


def get_author(user):
    return Author.objects.get_or_create(user=user)[0]


class AuthorHomeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return '/hero/'
        return f'/author/{get_author(self.request.user).pk}'


class AuthorDetailView(DetailView):
    template_name = 'author_detail.html'
    model = Author

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs.update(list_heroes(kwargs.get('object')))
        return kwargs


class AuthorAddView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/account_add.html'
    success_url = reverse_lazy('author_home')

class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "registration/account_edit.html"
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    success_url = reverse_lazy('author_home')


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "author_edit.html"
    model = Author
    fields = '__all__'
    success_url = reverse_lazy('author_home')

class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    template_name = 'author_delete.html'
    success_url = reverse_lazy('heroes')


class HeroListView(ListView):
    template_name = "hero/heroes.html"
    model = Hero
    fields = '__all__'

class HeroDetailView(DetailView):
    template_name = "hero/hero.html"
    model = Hero
    fields = '__all__'

class HeroCreateView(LoginRequiredMixin, CreateView):
    template_name = "hero/add.html"
    model = Hero
    fields = '__all__'
    success_url = reverse_lazy('author_home')

    def form_valid(self, form):
        form.instance.author = get_author(self.request.user)
        return super().form_valid(form)


class HeroUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "hero/edit.html"
    model = Hero
    fields = '__all__'
    success_url = reverse_lazy('author_home')


class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Hero
    template_name = 'hero/delete.html'
    success_url = reverse_lazy('author_home')

class MessageView(RedirectView):
    url = reverse_lazy('message_list')


class MessageListView(ListView):
    template_name = 'message/list.html'
    model = Message
    context_object_name = 'messages'


class MessageDetailView(DetailView):
    template_name = 'message/detail.html'
    model = Message
    context_object_name = 'message'


class MessageCreateView(LoginRequiredMixin, CreateView):
    template_name = "message/add.html"
    model = Message
    fields = '__all__'

    def form_valid(self, form):
        author = Author.objects.get_or_create(user=self.request.user)[0]
        form.instance.author = author
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "message/edit.html"
    model = Message
    fields = '__all__'


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = 'message/delete.html'
    success_url = reverse_lazy('message_list')