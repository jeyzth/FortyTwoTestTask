# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json
import django.utils.timezone as tz

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
    max_pk = latest_requests_list[0].pk
    context = {'latest_requests_list': latest_requests_list, 'max_pk': max_pk}
    return render(request, 'hello/requests10.html', context)


def chknewreq(request):
    latest_requests_list = MyRequest.objects.order_by('pk').reverse()[:10]
    data = {}
    cur_max_pk = latest_requests_list[0].pk
    data['cur_max_pk'] = cur_max_pk
    i = 0
    for req in latest_requests_list:
        i = 1 + i
        key = str(i) + "-1"
        data[key] = req.pk
        key = str(i) + "-2"
        dt = tz.localtime(req.query_dt)
        sd = "%.2d.%.2d.%.2d %.2d:%.2d:%.2d"
        sd = sd % (dt.day, dt.month, dt.year, dt.hour, dt.minute, dt.second)
        data[key] = sd
        key = str(i) + "-3"
        data[key] = req.remote_ip
        key = str(i) + "-4"
        data[key] = req.remote_host
        key = str(i) + "-5"
        data[key] = req.query_string

    if request.is_ajax():
        return HttpResponse(json.dumps(data), content_type="application/json")  # flake8: noqa
    else:
        return HttpResponse('no ajax')
