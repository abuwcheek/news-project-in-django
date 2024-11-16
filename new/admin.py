from django.contrib import admin
from .models import CategoryModel, TagModel, NewModel, AboutModel, ContactModel, AdsModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
     list_display = ('title', 'created_at', 'is_active')
     list_display_links = ('title', 'created_at')
     search_fields = ('title', 'created_at')
     list_editable=('is_active',)
     prepopulated_fields = {'slug': ['title']}




@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
     list_display = ('name', 'created_at', 'is_active')
     list_display_links = ('name', 'created_at')
     list_filter = ('is_featured',)
     search_fields = ('name', 'created_at')



@admin.register(NewModel)
class NewModelAdmin(admin.ModelAdmin):
     list_display = ('title', 'category', 'views', 'created_at', 'is_active')
     list_display_links = ('title', 'category', 'created_at')
     list_filter = ('is_featured', 'is_published')
     search_fields = ('title', 'category', 'views', 'created_at')
     list_editable=('is_active',)
     prepopulated_fields = {'slug': ['title']}
     readonly_fields = ('views',)
     filter_horizontal=('tags',)



@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
     list_display = ('email', 'phone_number', 'created_at', 'is_active')
     list_display_links = ('email', 'phone_number',)
     list_editable=('is_active',)



@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
     list_display = ('full_name', 'your_email', 'created_at', 'is_active')
     list_display_links = ('full_name', 'your_email',)
     search_fields = ('full_name', 'your_email')
     list_editable=('is_active',)



@admin.register(AdsModel)
class AdsModelAdmin(admin.ModelAdmin):
    list_display=('links', 'position', 'is_active')
    list_display_links=('links',)
    list_editable=('is_active', 'position')