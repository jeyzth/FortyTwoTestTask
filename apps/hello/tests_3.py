# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client

from hello.models import Contacts


class Tiket1TestAllFieldsOnPage(TestCase):
    def test_get_mainpage(self):
        """ Check no model in the database
        """
        del_rec = Contacts.objects.all()
        del_rec.delete()
        c = Client()
        response = c.get('http://localhost:8080')
        ucontent = response.content.decode('utf8')
        print ucontent
        assert(ucontent.find(u"не знайдено жодного запису") > 0)
