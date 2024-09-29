from django.db import models
from django.utils.text import slugify



class BaseModel(models.Model):
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     is_active = models.BooleanField(default=True)



class CategoryModel(BaseModel):
     title = models.CharField(max_length=200)
     slug = models.SlugField(null=True, blank=True)


     def __str__(self):
          return self.title


     def save(self, *args, **kwargs):
          if not self.slug:
               self.slug = slugify(self.title, allow_unicode=True)
          return super().save(*args, **kwargs)



class TagModel(BaseModel):
     name = models.CharField(max_length=200)


     def __str__(self):
          return self.name


     
class NewModel(BaseModel):
     category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True, related_name='category_new')
     title = models.CharField(max_length=200)
     slug = models.SlugField(null=True, blank=True)
     image = models.ImageField(upload_to='new_images/')
     description = models.TextField()
     body = models.TextField()
     tags = models.ManyToManyField(TagModel, blank=True)
     views = models.IntegerField(default=0)     


     def __str__(self):
          return f'{self.title} * {self.category}'

     
     def save(self, *args, **kwargs):
          if not self.slug:
               self.slug = slugify(self.title, allow_unicode=True)
          return super().save(*args, **kwargs)



class AboutModel(BaseModel):
     email = models.EmailField()
     phone_number = models.CharField(max_length=15)
     address = models.TextField()
     twitter = models.TextField()
     facebook = models.TextField()
     linkedin = models.TextField()
     instagram = models.TextField()
     youtube = models.TextField()
     telegram = models.TextField()


     def __str__(self):
          return f'{self.email} -> {self.phone_number}'



class ContactModel(BaseModel):
     full_name = models.CharField(max_length=50)
     your_email = models.EmailField()
     your_number = models.CharField(max_length=13)
     message = models.TextField()


     def __str__(self):
          return f'{self.full_name } == {self.your_email}'



class AdsModel(BaseModel):
     choices_pos = (
          ('one', 'ONE'),
     )
     image = models.ImageField(upload_to='ads_images/')
     links = models.CharField(max_length=100)
     position = models.CharField(max_length=5, choices=choices_pos)