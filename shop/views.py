from django.shortcuts import render
from shop.models import Item
from django.http import HttpResponse

def item_list(request):
    qs = Item.objects.all()
    return render(request, 'shop/item_list.html', {
    'item_list': qs,
})

def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))