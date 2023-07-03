from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('subpage/<slug:slug>',subpage,name='subpage')
]