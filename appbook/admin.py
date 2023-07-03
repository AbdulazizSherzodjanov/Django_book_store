from django.contrib import admin
from .models import *
class KategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Kategory,KategoryAdmin)
admin.site.register(Books,BooksAdmin)
