from .models import AboutModel, CategoryModel, TagModel

def index_processor(request):
    about = AboutModel.objects.first()
    category_list = CategoryModel.objects.all()
    tags = TagModel.objects.all().exclude().order_by('?')[:5]
    # ads_one=Ads.objects.all().filter(position='one', is_active=True).order_by('?')  

    context={

        'tags': tags,
        'about': about,
        'category_list': category_list,
        # 'ads_one': ads_one,
    }
    return context