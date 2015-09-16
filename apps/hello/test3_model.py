# -*- coding: utf-8 -*-
from django.utils.timezone import now
from django.test import TestCase
from django.test.client import Client

from hello.models import MyRequest


class Tiket3TestModel(TestCase):
    def test_add_rec(self):
        """  This test check model for next opertion
            Add 15 record into table DB
            with timeout 1 sec.
            After Add, test requests last 10 records.
            Delete records from table
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
        cnt = queries.count()
        print cnt
        i = 1

        for rec in queries:
            s = str(i) + "\t" + str(rec.pk) + "\t" + str(rec.query_dt)
            s = s + "\t" + rec.query_string
            i = i + 1

        assert(queries.count() == 10)

    def test_15_http_reqwuest(self):
        """ This test check how many record before
            and how many after it made 15 request.
        """
        c1 = Client()
        resp_r10_before = c1.get('http://localhost:8080/hello/requests10')
        resp_r10_before_ucontent = resp_r10_before.content.decode('utf8')
        c2 = Client()

        for i in range(1, 15):
            c2.get('http://localhost:8080/')

        c2 = Client()
        resp_r10_after = c2.get('http://localhost:8080/hello/requests10')
        resp_r10_after_ucontent = resp_r10_after.content.decode('utf8')
        print resp_r10_before_ucontent
        print resp_r10_after_ucontent
