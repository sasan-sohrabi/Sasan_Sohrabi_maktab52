from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'list_view'

urlpatterns = [
    path('', home_page, name='homepage'),
    path('menu/', menu, name='menu'),
    path('aboutus/', aboutus, name='aboutus'),
    path('contact/', contact, name='contact'),
    path('menuitem/', menuitem, name='menuitem'),
    path('menuitem2/', MenuItemsView.as_view(), name='menuitem2')
]
