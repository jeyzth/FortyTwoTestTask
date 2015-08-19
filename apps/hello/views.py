# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from hello.models import Contacts
from hello.models import MyRequest


def index(request):
    contact = get_object_or_404(Contacts, pk=1)
    context = {'contact': contact}
    return render(request, 'hello/index.html', context)


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
