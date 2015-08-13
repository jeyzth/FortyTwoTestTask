# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client


class Tiket1TestAllFieldsOnPage(TestCase):
    def test_get_mainpage(self):
        """  This test checks whether all fields models shown on the web page
             and correctly display Unicode Data.
        """
        c = Client()
        response = c.get('http://localhost:8080')
        ucontent = response.content.decode('utf8')
        """ print ucontent
        """
        assert(ucontent.find(u"Євген") > 0)
        assert(ucontent.find(u"Анонімов") > 0)
        assert(ucontent.find(u"9 березня 1973 р.") > 0)
        assert(ucontent.find(u"Shell") > 0)
        assert(ucontent.find(u"jeyzth@gmail.com") > 0)
        assert(ucontent.find(u"jeyzth@khavr.com") > 0)
        assert(ucontent.find(u"Delphi") > 0)
