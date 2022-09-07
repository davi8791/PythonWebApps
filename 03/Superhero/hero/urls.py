from django.urls import path
from .views import BlackWidow, HulkView, IndexView, IronManView, ScarletWitchView, SpiderManView

urlpatterns = [
    path('', IndexView.as_view()),
    path('hulk', HulkView.as_view()),
    path('ironman', IronManView.as_view()),
    path('blackwidow', BlackWidow.as_view()),
    path('scarletwitch', ScarletWitchView.as_view()),
    path('spiderman', SpiderManView.as_view()),
]
