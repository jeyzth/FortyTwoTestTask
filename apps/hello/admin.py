from django.contrib import admin

# Register your models here.
from hello.models import Contacts
from hello.models import MyRequest

admin.site.register(Contacts)

admin.site.register(MyRequest)
