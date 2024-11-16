from django.urls import path
from .views import IndexView, SinglePageView, AboutView, ContactView, CategoryDetailView, SearchView


urlpatterns = [
     path('list/', IndexView.as_view(), name='index'),
     path('categories/<str:slug>/', CategoryDetailView.as_view(), name='ctgdetail'),
     path('single/<str:slug>/', SinglePageView.as_view(), name='detailurl'),
     path('about/', AboutView.as_view(), name='abouturl'),
     path('contact/', ContactView.as_view(), name='contacturl'),
     path('search/', SearchView.as_view(), name='searchurl'),
]