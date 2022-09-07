from django.urls import path
from .views import IndexView, ScarletWitchView, SpiderManView, MantisView

urlpatterns = [
    path('', IndexView.as_view()),
    path('scarletwitch', ScarletWitchView.as_view()),
    path('spiderman', SpiderManView.as_view()),
    path('mantis', MantisView.as_view()),
]
