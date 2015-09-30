# -*- coding: utf-8 -*-
from django.utils.timezone import now
from django.test import TestCase
from django.test.client import Client

from hello.models import MyRequest


class Tiket3TestModel(TestCase):
    def test_add_rec(self):
        """ This test checks model MyRequest and view data frome this model.
            for next opertion Add 15 record into table DB
            with timeout 1 sec. After Add, test requests last 10 records.
        """
        for i in range(1, 15):
            new_rec = MyRequest(
                query_dt=now(),
                remote_ip="127.0.0.1",
                remote_host=str(i),
                query_string=u"http://localhost/hello/"+str(i)
            )
            new_rec.save()

        queries = MyRequest.objects.order_by('pk').reverse()[:10]
        self.assertEqual(queries.count(), 10)

    def test_15_http_reqwuest(self):
        """ This test checks midleware keeps query in the model MyRequests
            For this test, saved pages content request10 before 15th requests
            to the home page and after it Both content have variable Max_PK
            (Max value PrimaryKey). Max_PK diference from different contents
            should match the number of queries to the home page.
        """
        c1 = Client()
        resp_r10_before = c1.get('http://localhost:8080/hello/requests10')
        resp_r10_before_ucontent = resp_r10_before.content.decode('utf8')
        c2 = Client()

        for i in range(1, 16):
            c2.get('http://localhost:8080/')

        c2 = Client()
        resp_r10_after = c2.get('http://localhost:8080/hello/requests10')
        resp_r10_after_ucontent = resp_r10_after.content.decode('utf8')
        s1 = resp_r10_before_ucontent
        s1 = s1.replace(u' ', u'')
        s2 = resp_r10_after_ucontent
        s2 = s2.replace(u' ', u'')
        i = s1.find(u'max_pk=')
        ln = len(u'max_pk=')
        j = s1.find(u';', i)
        i = i + ln
        s1 = s1[i:j]
        i = s2.find(u'max_pk=') + ln
        j = s2.find(u';', i)
        s2 = s2[i:j]
        self.assertEqual(int(s2)-int(s1), 15)
