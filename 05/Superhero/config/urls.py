from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path


from hero.views import HeroListView, HeroDetailView


urlpatterns = [

    # Home
    path('', RedirectView.as_view(url='hero/')),

    # Photos
    path('hero/', HeroListView.as_view()),
    path('hero/<int:pk>', HeroDetailView.as_view()),

    # Admin
    path('admin/', admin.site.urls)
]
