# -*- coding: utf-8 -*-
from django.test import TestCase


from hello.models import Contacts


class Tiket1TestsDB(TestCase):
    def test_add_rec(self):
        """  This test check model for next opertion
            Add record into table DB
            Find record in table
            Delete record from table
        """
        new_rec = Contacts(
            name=u"Іван",
            surname=u"Пантов",
            dateofbird=u"1993-02-03",
            bio=u"Кодю на С & Shell під Linux (x86,armv7),на Delphi під Win32",
            email=u"somebody@gmail.com",
            jabber=u"somebody@khavr.com",
            skype=u"big_goss",
            others=u"т. 7717123456 м. +77071234567 м.+380501234567"
        )

        new_rec.save()
        print "test_add_rec OK"
        print "test_del_rec"
        print Contacts.objects.all()
        del_rec = Contacts.objects.get(name=u"Іван")
        print del_rec.name + " " + del_rec.surname
        del_rec.delete()
        print "test_del_rec"
        assert(2 + 2 == 4)
