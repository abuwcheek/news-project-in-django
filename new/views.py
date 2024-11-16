from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db.models import Q
from django.contrib import messages
from .models import CategoryModel, TagModel, NewModel, AboutModel, ContactModel, AdsModel



class CategoryModelListView(View):
     def get(self, request):
          ctg_list = CategoryModel.objects.all()

          context = {
               'ctg_list': ctg_list,
          }
          return render(request, 'base.html', context)



class CategoryDetailView(View):
     def get(self, request, slug):
          category_news = get_object_or_404(CategoryModel, slug=slug)
          ctg_detail = category_news.category_new.all()

          context = {
               'category_news': category_news,
               'ctg_detail': ctg_detail,
          }
          return render(request, 'category_list.html', context)



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
          
          detail_news.views += 1
          detail_news.save()

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



class ContactView(View):
     def get(self, request):
          return render(request, 'contact.html')

     
     def post(self, request):
          data=request.POST
          contact=ContactModel()

          contact.full_name = data.get('name')
          contact.your_email = data.get('email')
          contact.your_number = data.get('number')
          contact.message = data.get('message')
          if int(contact.your_number) > 13:
               messages.warning(request, "Nomer xato kiritildi")
               return render(request, 'contact.html')
          elif int(contact.your_number) < 13:
               messages.warning(request, "Nomer xato kiritildi")
               return render(request, 'contact.html')


          contact.save()

          messages.success(request, "Ma'lumotlaringiz yuborildi.")
          return redirect('index')




class SearchView(View):
    def get(self, request):
          query = request.GET.get('query')
          if not query:
               return redirect('index')

          news = NewModel.objects.all().filter(Q(title__icontains = query) | Q(description__icontains = query) | Q(body__icontains = query))
          if not news:
               messages.warning(request, "So'rov bo'yicha xabar topilmadi")
               return redirect('index')

          context = {
               'searchnews': news 
          }
          messages.info(request, 'Siz izlagan xabarlar')
          return render(request, 'search.html', context)
