from django.contrib import admin

# Register your models here.
from hello.models import Contacts


admin.site.register(Contacts)