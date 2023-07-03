from django.shortcuts import render

from .models import *


def home(request):
    b = Books.objects.all().order_by('-id')
    c = Kategory.objects.all()
    newbook = Books.objects.all().order_by('-date_added').first()
    best_book = Books.objects.all().order_by('-id')
    ctx = {
        'book': b,
        'cat': c,
        'new': newbook,
        'best': best_book
    }
    return render(request, 'home.html', ctx)


def subpage(request, slug):
    k = Books.objects.get(slug=slug)
    c = Kategory.objects.all()
    newbook = Books.objects.all().order_by('-date_added').first()
    best_book = Books.objects.all().order_by('-id')
    ctx = {
        'k': k,
        'cat': c,
        'new': newbook,
        'best': best_book
    }
    return render(request, 'subpage.html', ctx)
