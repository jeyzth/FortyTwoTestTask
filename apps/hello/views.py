# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


from hello.models import Contacts
from hello.models import MyRequest


def index(request):
    try:
        contact = Contacts.objects.order_by('pk')[0]
        context = {'contact': contact}
        return render(request, 'hello/index.html', context)
    except:
        return render(request, 'hello/emptytable.html', None)


def requests10(request):
    latest_requests_list = MyRequest.objects.order_by('pk').reverse()[:10]
    context = {'latest_requests_list': latest_requests_list}
    return render(request, 'hello/requests10.html', context)


def chknewreq(request):
    lrl = MyRequest.objects.order_by('pk').reverse()[:1]
    cur_max_pk = lrl[0].pk
    if request.is_ajax():
        return HttpResponse(str(cur_max_pk))
    else:
        return HttpResponse('no ajax')
