# -*- coding: utf-8 -*-

from django.shortcuts import render,get_object_or_404


from hello.models import Contacts

# Create your views here.


def index(request):
    contacts = [Contacts.objects.get(name=u'Євген')]
    context = {'contacts': contacts}
    return render(request, 'hello/index.html', context)

def h404(request):
    contacts = get_object_or_404(Contacts, name=u'Євген')
    return render(request, 'hello/h404.html', {'contacts': contacts})