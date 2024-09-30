from django.urls import path
from .views import IndexView, AboutView


urlpatterns = [
     path('list/', IndexView.as_view(), name='index'),
     path('about/', AboutView.as_view(), name='abouturl'),
]