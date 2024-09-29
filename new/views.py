from django.shortcuts import render
from django.views import View
from .models import CategoryModel, TagModel, NewModel, AboutModel, ContactModel, AdsModel



class CategoryModelListView(View):
     def get(self, request):
          ctg_list = CategoryModel.objects.all().filter(is_active=True)

          context = {
               'ctg_list': ctg_list,
          }
          return render(request, 'base.html', context)



class IndexView(View):
     def get(self, request):
          return render(request, 'index.html')