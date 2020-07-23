from django.shortcuts import render
from .models import Item
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def item_list(request):
    qs = Item.objects.all()
    q = request.GET.get('q','')
    if q:
        qs = qs.filter(name__icontains=q)

    logger.debug('query : {}'.format(q))
    return render(request, 'shop/item_list.html', {
        'item_list': qs,
        'q':q,
     })

def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))