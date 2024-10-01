from django.shortcuts import render, redirect, get_object_or_404
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
          news = NewModel.objects.all().filter(is_active=True).order_by('?')[:5]
          
          sports = NewModel.objects.filter(category__title='Sports')[:3]
          technology = NewModel.objects.filter(category__title='Technology')[:3]
          business = NewModel.objects.filter(category__title='Business')[:3]
          entertainment = NewModel.objects.filter(category__title='Entertainment')[:3]
          political_news = NewModel.objects.filter(category__title='Political news')

          featured_news = NewModel.objects.filter(is_featured=True)[:3]
          popular_news = NewModel.objects.filter(is_active=True).order_by('-views')[:3]
          latest_news = NewModel.objects.filter(is_active=True).order_by('-created_at')[:3]

          most_viewed = NewModel.objects.all().filter(is_active=True).exclude(views=100)[:3]
          most_read = NewModel.objects.all().filter(is_active=True).order_by('-updated_at')[:3]
          most_recent = NewModel.objects.exclude(is_published=True)[:3]

          random_news = NewModel.objects.exclude(is_published=True)[:9]



          context = {
               'news': news,
               'sports': sports,
               'technology': technology,
               'business': business,
               'entertainment': entertainment,
               'political_news': political_news,

               'featured_news': featured_news,
               'popular_news': popular_news,
               'latest_news': latest_news,

               'most_viewed': most_viewed,
               'most_read': most_read,
               'most_recent': most_recent,

               'random_news': random_news,
          }
          return render(request, 'index.html', context)



class SinglePageView(View):
     def get(self, request, slug):
          detail_news = get_object_or_404(NewModel, slug=slug)
          other_news = NewModel.objects.order_by('?')[:4]
          this_ctg = NewModel.objects.exclude(is_published=False)[:4]
          # ctg_count = detail_news.category_new.filter(is_active=True).count()
          ctg_count = NewModel.objects.values('category').count()

          
          featured_news = NewModel.objects.filter(is_featured=False)[:4]
          popular_news = NewModel.objects.filter(is_active=True).order_by('-views')[:4]
          latest_news = NewModel.objects.filter(is_active=True).order_by('-created_at')[:4]
          

          context = {
               'detail_news': detail_news,
               'other_news': other_news,
               'this_ctg': this_ctg,
               'ctg_count': ctg_count,
               
               'featured_news': featured_news,
               'popular_news': popular_news,
               'latest_news': latest_news,
          }
          return render(request, 'single-page.html', context)

class AboutView(View):
     def get(self, request):
          about = AboutModel.objects.all()
          context = {
               'about': about,
          }
          return render(request, 'base.html', context)