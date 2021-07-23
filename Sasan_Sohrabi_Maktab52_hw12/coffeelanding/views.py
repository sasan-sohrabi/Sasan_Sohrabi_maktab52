import json
from datetime import date
from json import dumps

from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views import View, generic
from django.views.decorators.csrf import csrf_exempt

from .forms import MenuForm, MenuForm2
from .models import Category, Order, Menu_items, SubOrder, Tables

from django.utils.translation import gettext as _


# Create your views here.

# Home Page
def home_page(request):
    return render(request, 'home1.html')


# Menu Page
def menu(request):
    if request.method == 'POST':
        orders = json.loads(request.body.decode('utf-8'))
        orderid = Order.objects.create(date_serve=timezone.now(), status=True, table_order_id=orders['table'])
        for item in orders['items']:
            SubOrder.objects.create(count=orders['items'][item]['quantity'], menu_items_id=item, order_id=orderid)
        return render(request, 'main_menu.html')

    menu_data = Menu_items.objects.all()
    menu_item_dic = {}
    for menu_element in menu_data:
        menu_item_dic[menu_element.id] = {"name": menu_element.name, "category": menu_element.category_id_id,
                                          "price": menu_element.price, 'img': str(menu_element.img)}
    menuJson = dumps(menu_item_dic)
    return render(request, 'main_menu.html', {'data': menuJson})


# About Us Page
def aboutus(request):
    return render(request, 'aboutus.html')


# Contact Page
def contact(request):
    return render(request, 'contact.html')


def detail_list(request, id):
    data_suborder = SubOrder.objects.filter(order_id__suborder=id)
    menu_items = Menu_items.objects.filter(suborder__order_id=id)
    return render(request, 'detail_list.html', {'detail_list': data_suborder, 'menuitems': menu_items})


class MenuAddView(View):
    def get(self, *args, **kwargs):
        menuitems = Menu_items.objects.all()
        return render(self.request, 'order_add.html', {'menuitems': menuitems})

    @csrf_exempt
    def post(self, *args, **kwargs):
        print(kwargs)
        return HttpResponse("add")


def menuitem(request):
    if request.method == "GET":
        form = MenuForm()
        return render(request, 'MenuItemadd.html', {'form': form})

    elif request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            img = form.cleaned_data['image']
            default_storage.save(img.name, img)
            Menu_items.objects.create(name=form.cleaned_data['name'], price=form.cleaned_data['price'],
                                      discount=form.cleaned_data['discount'],
                                      category_id=Category.objects.get(id=int(form.cleaned_data['category'])),
                                      available=form.cleaned_data['available'], date_serve=timezone.now(),
                                      cooking_time_estimate=timezone.now(), img=img.name)
            return HttpResponse("Great!!!")
        else:
            return render(request, 'MenuItemadd.html', {'form': form})

class MenuItemsView(generic.FormView):
    template_name = 'menuitem_2.html'
    form_class = MenuForm2
    success_url = 'https://www.google.com/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)




