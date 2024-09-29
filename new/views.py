from django.shortcuts import render
from django.views import View
from .models import CategoryModel, TagModel, NewModel, AboutModel, ContactModel, AdsModel



class CategoryModelListView(View):
     def get(self, request):
          ctg_list = CategoryModel.objects.all()

          context = {
               'ctg_list': ctg_list,
          }
          return render(request, 'base.html', context)



class IndexView(View):
     def get(self, request):
          news = NewModel.objects.all().filter(is_active=True).order_by('?')[:6]
          sports = NewModel.objects.filter(category__title='Sports')[:3]
          technology = NewModel.objects.filter(category__title='Technology')[:3]
          business = NewModel.objects.filter(category__title='Business')[:3]
          entertainment = NewModel.objects.filter(category__title='Entertainment')[:3]
          political_news = NewModel.objects.filter(category__title='	Political news')[:3]

          context = {
               'news': news,
               'sports': sports,
               'technology': news,
               'business': business,
               'entertainment': entertainment,
               'political_news': political_news,
          }
          return render(request, 'index.html', context)