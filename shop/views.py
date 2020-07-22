from django.shortcuts import render
from .models import Item
from django.http import HttpResponse

def item_list(request):
    qs = Item.objects.all()
    q = request.GET.get('q','')
    if q:
        qs = qs.filter(name__icontains=q)
    return render(request, 'shop/item_list.html', {
        'item_list': qs,
        'q':q,
     })

def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))