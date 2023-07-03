from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Kategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Kategoriyalar'

    def __str__(self):
        return self.name
    
class Books(models.Model):
    cat_id = models.ForeignKey(Kategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    page = models.IntegerField()
    publish_date = models.DateTimeField(auto_now_add=False)
    book_of_author = models.CharField(max_length=255)
    price = models.IntegerField()
    slug = models.SlugField(max_length=255, unique=True, null=True)
    body = RichTextUploadingField()
    post_img = models.ImageField(upload_to='posts')
    date_added = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files')

    class Meta:
        verbose_name_plural = 'Kitoblar'

    def __str__(self):
        return self.title