from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import include, path

from hero.views import HeroListView, HeroDetailView, HeroCreateView, HeroUpdateView, HeroDeleteView, InvestigatorHomeView, InvestigatorDetailView, InvestigatorAddView, InvestigatorUpdateView, InvestigatorDeleteView, UserUpdateView


urlpatterns = [

    path('accounts/', include('django.contrib.auth.urls')),

    # Investigator
    path('',                           RedirectView.as_view(url='investigator/home')),
    path('investigator/home',                InvestigatorHomeView.as_view(),    name='investigator_home'),
    path('investigator/<int:pk>',            InvestigatorDetailView.as_view(),  name='investigator_detail'),
    path('investigator/<int:pk>/',           InvestigatorUpdateView.as_view(),  name='investigator_edit'),
    path('investigator/<int:pk>/delete',     InvestigatorDeleteView.as_view(),  name='investigator_delete'),

    # Hero
    path('hero/',                HeroListView.as_view(),    name='hero_list'),
    path('hero/<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('hero/add',             HeroCreateView.as_view(),  name='hero_add'),
    path('hero/<int:pk>/edit',   HeroUpdateView.as_view(),  name='hero_edit'),
    path('hero/<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),

    # Login/Sign Up
    path('signup/',                InvestigatorAddView.as_view(),     name='sign_up'),


]
