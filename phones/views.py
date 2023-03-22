from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from phones.models import Phone

def index(request):
    return redirect('catalog')

# Для реализации сортировки можно к урлу добавить параметр sort и получать его через request.GET. Например:
#
# <имя_сайта>/catalog?sort=name - сортировка по названию
# <имя_сайта>/catalog?sort=min_price - сначала отображать дешевые

def show_catalog(request):
    sort = request.GET.get('sort')
    if sort == 'name':
        my_objects = Phone.objects.all().order_by('name')
        print(Phone.objects.all().order_by('name'))
    elif sort == 'min_price':
        my_objects = Phone.objects.all().order_by('price')
        print(Phone.objects.all().order_by('-price'))
    elif sort == 'max_price':
        my_objects = Phone.objects.all().order_by('-price')
        print(str(Phone.objects.all().order_by('price')))
    else:
        my_objects = Phone.objects.all()
    template = 'catalog.html'
    context = {
        'phones': my_objects
    }
    return render(request, template, context)

def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    template = 'product.html'
    context = {
        'phone': phone
    }
    return render(request, template, context)


#
# def show_catalog(request):
#     template = 'catalog.html'
#     context = {}
#     return render(request, template, context)
#
#
# def show_product(request, slug):
#     template = 'product.html'
#     context = {}
#     return render(request, template, context)
