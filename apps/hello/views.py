from django.http import HttpResponse
from django.template import RequestContext, loader

from hello.models import Contacts

# Create your views here.


def index(request):
    contacts = Contacts.objects.order_by('name')
    template = loader.get_template('hello/index.html')
    context = RequestContext(request, {
        'contacts': contacts,
    })
    return HttpResponse(template.render(context))
