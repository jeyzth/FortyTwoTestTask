# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client


from hello.models import Contacts


class Tiket1Test(TestCase):

    def test_get_mainpage(self):
        """  This test checks whether all fields models shown on the web page
             and correctly display Unicode Data.
        """
        contact = Contacts.objects.order_by('pk')[0]
        c = Client()
        response = c.get('http://localhost:8080')
        ucontent = response.content
        s2 = ucontent
        s2 = unicode(s2, 'utf8', 'ignore')
        self.assertIn(contact.name, s2)
        self.assertIn(contact.surname, s2)
        sbio = contact.bio
        sbio = sbio.replace(u'\n', u'<br />')
        sbio = sbio.replace(u'&', u'&amp;')
        sbio = sbio.replace(u'\'', u'&#39;')
        self.assertIn(sbio, s2)
        self.assertIn(contact.email, s2)
        self.assertIn(contact.jabber, s2)
        self.assertIn(contact.skype, s2)
        s_others = contact.others
        s_others = s_others.replace(u'\n', u'<br />')
        self.assertIn(s_others, s2)

    def test_sinle_result(self):
        """ Showing a single entry, even if a few.
        """
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
        new_rec3.save()
        c = Client()
        response = c.get('http://localhost:8080')
        ucontent = response.content.decode('utf8')
        assert(ucontent.find(u"Алдар") < 0)
        assert(ucontent.find(u"Косе") < 0)
        assert(ucontent.find(u"9 березня 1973 р.") > 0)
        assert(ucontent.find(u"jeyzth@gmail.com") > 0)
        assert(ucontent.find(u"jeyzth@khavr.com") > 0)
        assert(ucontent.find(u"hodzha") < 0)
        assert(ucontent.find(u"nasredin") < 0)

    def test_page_ws_empty_table(self):
        """ Check no model in the database
        """
        del_rec = Contacts.objects.all()
        del_rec.delete()
        c = Client()
        response = c.get('http://localhost:8080')
        ucontent = response.content.decode('utf8')
        assert(ucontent.find(u"не знайдено жодного запису") > 0)

    def test_context(self):
        """ Check key (field of model) in dictionary (context)
        """
        contact = Contacts.objects.order_by('pk')[0]
        context = {'contact': contact}
        self.assertEqual(hasattr(context['contact'], 'name'), True)
        self.assertEqual(hasattr(context['contact'], 'surname'), True)
        self.assertEqual(hasattr(context['contact'], 'dateofbird'), True)
        self.assertEqual(hasattr(context['contact'], 'bio'), True)
        self.assertEqual(hasattr(context['contact'], 'email'), True)
        self.assertEqual(hasattr(context['contact'], 'skype'), True)
        self.assertEqual(hasattr(context['contact'], 'jabber'), True)
        self.assertEqual(hasattr(context['contact'], 'others'), True)
