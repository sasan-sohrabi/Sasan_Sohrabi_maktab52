from django.contrib import admin
from .models import Category, Tables, Order, Menu_items, SubOrder, Receipt

# Register your models here.
admin.site.register(Category)
admin.site.register(Tables)
admin.site.register(Order)
admin.site.register(Menu_items)
admin.site.register(SubOrder)
admin.site.register(Receipt)
