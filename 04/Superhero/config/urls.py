from django.views.generic import RedirectView
from django.urls import path

from hero.views import HeroListView, HeroDetailView


urlpatterns = [

    # Home
    path('', RedirectView.as_view(url='hero/')),

    # Photos
    path('hero/', HeroListView.as_view()),
    path('hero/<str:hero_name>', HeroDetailView.as_view()),
]
