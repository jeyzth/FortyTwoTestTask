# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404


from hello.models import Contacts


def index(request):
    contact = get_object_or_404(Contacts, pk=1)
    context = {'contact': contact}
    return render(request, 'hello/index.html', context)
