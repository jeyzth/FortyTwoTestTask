# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client

from hello.models import Contacts


class Tiket1TestAllFieldsOnPage(TestCase):
    def test_get_mainpage(self):
        """ This test appearance messedzha should check that the page was
            not found when the field name does not correspond to that given
            in view.
        """
        sbio = u"Кодю на С and Shell під Linux (x86,armv7),на Delphi під Win32"
        sothr = u"т. 7717123456 м. +77071234567 м.+380501234567"
        new_rec = Contacts(
            name=u"Василь",
            surname=u"Анонімов",
            dateofbird=u"1973-02-03",
            bio=sbio,
            email=u"jeyzth@gmail.com",
            jabber=u"jeyzth@khavr.com",
            skype=u"ghost",
            others=sothr
        )

        new_rec.save()
        c = Client()
        response = c.get('http://localhost:8080')
        ucontent = response.content.decode('utf8')
        """print ucontent
        """
        assert(ucontent.find(u"Page Not Found") > 0)
