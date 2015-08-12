# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client

from hello.models import Contacts


class Tiket1TestAllFieldsOnPage(TestCase):
    def test_get_mainpage(self):
        """ This test must to check
            Showing a single entry, even if several base
        """
        sbio = u"Кодю на С and Shell під Linux (x86,armv7),на Delphi під Win32"
        sothr = u"т. 7717123456 м. +77071234567 м.+380501234567"

        new_rec1 = Contacts(
            name=u"Алдар",
            surname=u"Косе",
            dateofbird=u"1968-02-09",
            bio="Хитрий і проворний",
            email=u"aldar@satu.kz",
            jabber=u"aldar@xmpp.kz",
            skype=u"aldar.kose",
            others="Хтозна"
        )

        new_rec2 = Contacts(
            name=u"Євген",
            surname=u"Анонімов",
            dateofbird=u"1973-02-03",
            bio=sbio,
            email=u"jeyzth@gmail.com",
            jabber=u"jeyzth@khavr.com",
            skype=u"ghost",
            others=sothr
        )

        new_rec3 = Contacts(
            name=u"Ходжа",
            surname=u"Насрідін",
            dateofbird=u"1963-07-04",
            bio="Дуже язикатий",
            email=u"hodzha@satu.uz",
            jabber=u"hodzha@xmpp.uz",
            skype=u"hodzha.nasredin",
            others="Дезна"
        )

        new_rec1.save()
        new_rec2.save()
        new_rec3.save()
        c = Client()
        response = c.get('http://localhost:8080')
        ucontent = response.content.decode('utf8')
        print ucontent
        assert(ucontent.find(u"Алдар") < 0)
        assert(ucontent.find(u"Косе") < 0)
        assert(ucontent.find(u"3 лютого 1973 р.") > 0)
        assert(ucontent.find(sbio) > 0)
        assert(ucontent.find(u"jeyzth@gmail.com") > 0)
        assert(ucontent.find(u"jeyzth@khavr.com") > 0)
        assert(ucontent.find(u"hodzha") < 0)
        assert(ucontent.find(u"nasredin") < 0)
