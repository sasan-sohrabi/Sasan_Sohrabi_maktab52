from django.contrib.auth.models import User
from django.db import models


# Create your models here.

# 1- Create Category table
from django.utils import timezone


class Category(models.Model):
    category_name = models.CharField(max_length=30)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}# category_name: {self.category_name}, category_parent: {self.parent_category}"




# 2- Create Menu_items table
class Menu_items(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name of menu item', help_text="Import name of menu item")
    price = models.FloatField(verbose_name='Price of item', help_text='Price of item')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount = models.FloatField(verbose_name='Discount of item', help_text='Discount of item')
    date_serve = models.DateTimeField(verbose_name='Date', help_text='Data of creation', null=True)
    cooking_time_estimate = models.TimeField(verbose_name='Time', help_text='Time spend to prepare', null=True)
    available = models.BooleanField(default=False, verbose_name='Available', help_text='Is item available')
    img = models.FileField(upload_to='menu_items/', verbose_name="Address", help_text="Address of image", default=None,
                           null=True)

    def __str__(self):
        return f"{self.id}# name: {self.name}"

    @classmethod
    def filter_by_category(cls, category):
        return cls.objects.filter(category_id__parent_category__category_name=category)

    def final_price(self):
        return self.price - self.discount


# 3- Create Tables table
class Tables(models.Model):
    space_position = models.IntegerField(verbose_name='Position of table', help_text='Position of table in coffee shop')
    capacity = models.IntegerField(verbose_name='Capacity', help_text='Number of people can use table')

    def __str__(self):
        return f"{self.id}# space_position: {self.space_position}"


# 4- Create Order table
class Order(models.Model):
    table_order = models.ForeignKey(Tables, on_delete=models.CASCADE, verbose_name='Table ordered',
                                    help_text='In which table ordered ...?')
    date_serve = models.DateTimeField(verbose_name='Date of order', help_text='When customer ordered ...?')
    status = models.BooleanField(verbose_name='Status', help_text='Status of order, exp.: WAITING, REQ and ...')

    def __str__(self):
        return f"{self.id}# table_order: {self.table_order}, status: {self.status}"

    @classmethod
    def filter_by_menuitem(cls, menu_item):
        return cls.objects.filter(suborder__menu_items__name=menu_item)

    @classmethod
    def filter_by_menuitem_category(cls, category):
        return cls.objects.filter(suborder__menu_items__category_id__category_name=category)


    @classmethod
    def filter_by_today_orders(cls):
        return cls.objects.filter(date_serve=timezone.now)



# 5- Crete SubOrder table
class SubOrder(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Order id',
                                 help_text='Related to which order?')
    menu_items = models.ForeignKey(Menu_items, on_delete=models.CASCADE, verbose_name='Menu item id',
                                   help_text='Related to which menu item?')
    count = models.IntegerField(verbose_name='Count', help_text='Count of product in order?')

    def __str__(self):
        return f"{self.id}# order_id: {self.order_id}, menu_items: {self.menu_items}, count: {self.count}"


# 6- Create Receipt table
class Receipt(models.Model):
    orders = models.ForeignKey(Order, on_delete=models.CASCADE)
    total_price = models.FloatField()
    final_price_with_discount = models.FloatField()
    time_stamps = models.DateTimeField()

    def __str__(self):
        return f" {self.id}# {self.orders} {self.total_price} {self.final_price_with_discount} {self.time_stamps}"


