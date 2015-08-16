# -*- coding: utf-8 -*-
from django.utils.timezone import now
from django.test import TestCase


from hello.models import MyRequest


class Tiket3TestModel(TestCase):
    def test_add_rec(self):
        """  This test check model for next opertion
            Add 15 record into table DB
            with timeout 1 sec.
            After Add request last 10 records.
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
            print str(i)+"\t"+str(rec.query_dt)+"\t"+rec.query_string
            i = i+1

        assert(queries.count() == 10)
