from datetime import date
from django import forms
from django.forms import ModelForm,widgets
from hello.models import Contacts
import fortytwo_test_task.settings
from django.contrib.admin.widgets import AdminDateWidget

class DateSelectorWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):
        # create choices for days, months, years
        # example below, the rest snipped for brevity.
        years = [(year, year) for year in (2011, 2012, 2013)]
        _widgets = (
            widgets.Select(attrs=attrs, choices=date.day),
            widgets.Select(attrs=attrs, choices=date.month),
            widgets.Select(attrs=attrs, choices=date.year),
        )
        super(DateSelectorWidget, self).__init__(_widgets, attrs)
                                                                                        
    def decompress(self, value):
        if value:
            return [value.day, value.month, value.year]
        return [None, None, None]
        
    def format_output(self, rendered_widgets):
         return u''.join(rendered_widgets)

    def value_from_datadict(self, data, files, name):
        datelist = [
            widget.value_from_datadict(data, files, name + '_%s' % i)
            for i, widget in enumerate(self.widgets)]
        try:
            D = date(
                day=int(datelist[0]), 
                month=int(datelist[1]),
                year=int(datelist[2]))
        except ValueError:
            return ''
        else:
            return str(D)

class FormContact(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormContact,self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'}),
        self.fields['surname'].widget.attrs.update({'class': 'form-control'}),
        self.fields['bio'].widget.attrs.update({'class': 'form-control'}),
        self.fields['email'].widget.attrs.update({'class': 'form-control'}),
        self.fields['jabber'].widget.attrs.update({'class': 'form-control'}),
        self.fields['dateofbird'].widget.attrs.update({'class': 'datepicker'}),
        self.fields['skype'].widget.attrs.update({'class': 'form-control'}),
        self.fields['others'].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Contacts
        fields = ['name','surname','dateofbird','bio','email','jabber','skype','others']
        #widjets = {'dateofbird': AdminDateWidget(attrs={'class':'date_picker'})
        widgets = {'dateofbirth': forms.DateInput(attrs={'class': 'datepicker'})
                                     
        }


        
"""        
forms.DateInput(attrs={'class':'date_picker'}
"""
 