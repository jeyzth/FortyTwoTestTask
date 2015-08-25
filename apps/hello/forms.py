from django.forms import ModelForm
from hello.models import Contacts


class FormContact(ModelForm):
    class Meta:
        model = Contacts
        fields = ['name','surname','dateofbird','bio','email','jabber','skype','others']

 