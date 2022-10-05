from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path
from django.urls import include, path

from hero.views import HeroListView, HeroDetailView, HeroCreateView, HeroUpdateView, HeroDeleteView, AuthorHomeView, AuthorDetailView, AuthorAddView, AuthorUpdateView, AuthorDeleteView, UserUpdateView


urlpatterns = [

    # Accounts
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/<int:pk>/',          UserUpdateView.as_view(),  name='user_edit'),

    # Author
    path('',                           RedirectView.as_view(url='author/home')),
    path('author/home',                AuthorHomeView.as_view(),    name='author_home'),
    path('author/<int:pk>',            AuthorDetailView.as_view(),  name='author_detail'),
    path('author/add/',                AuthorAddView.as_view(),     name='author_add'),
    path('author/<int:pk>/',           AuthorUpdateView.as_view(),  name='author_edit'),
    path('author/<int:pk>/delete',     AuthorDeleteView.as_view(),  name='author_delete'),

    # Hero
    path('hero/',                HeroListView.as_view(),    name='hero_list'),
    path('hero/<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('hero/add',             HeroCreateView.as_view(),  name='hero_add'),
    path('hero/<int:pk>/edit',       HeroUpdateView.as_view(),  name='hero_edit'),
    path('hero/<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),


]
