from .models import AboutModel, CategoryModel, TagModel, AdsModel

def index_processor(request):
    about = AboutModel.objects.first()
    category_list = CategoryModel.objects.all()
    tags = TagModel.objects.all().exclude(is_featured=False).order_by('?')[:5]
    another_tags = TagModel.objects.all().exclude(is_featured=True).order_by('?')[:8]
    ads_one=AdsModel.objects.all().filter(position='one', is_active=True).order_by('?')[:1] 

    context={

        'tags': tags,
        'another_tags': another_tags,
        'about': about,
        'category_list': category_list,
        'ads_one': ads_one,
    }
    return context