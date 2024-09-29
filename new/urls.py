from django.urls import path
from .views import IndexView


urlpatterns = [
     path('list/', IndexView.as_view(), name='index')
]