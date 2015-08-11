# -*- coding: utf-8 -*-

from django.shortcuts import render


from hello.models import Contacts

# Create your views here.


def index(request):
    contacts = [Contacts.objects.get(name=u'Євген')]
    #template = loader.get_template('hello/index.html')
    #context = RequestContext(request, {
    #    'contacts': contacts,
    #}
    context ={'contacts': contacts}
    return render(request,'hello/index.html',context)
