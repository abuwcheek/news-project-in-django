from django.urls import path
from .views import IndexView, SinglePageView, AboutView


urlpatterns = [
     path('list/', IndexView.as_view(), name='index'),
     path('single/<str:slug>/', SinglePageView.as_view(), name='detailurl'),
     path('about/', AboutView.as_view(), name='abouturl'),
]