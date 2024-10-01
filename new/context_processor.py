from .models import AboutModel, CategoryModel, TagModel, AdsModel

def index_processor(request):
    about = AboutModel.objects.first()
    category_list = CategoryModel.objects.all()
    tags = TagModel.objects.all().exclude().order_by('?')[:4]
    ads_one=AdsModel.objects.all().filter(position='one', is_active=True).order_by('?')[:1] 

    context={

        'tags': tags,
        'about': about,
        'category_list': category_list,
        'ads_one': ads_one,
    }
    return context