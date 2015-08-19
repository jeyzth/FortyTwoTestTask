from django.db import models

# Create your models here.


class Contacts(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    dateofbird = models.DateField()
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length=20)
    others = models.TextField()


class MyRequest(models.Model):
    query_dt = models.DateTimeField([False, True])
    remote_ip = models.IPAddressField()
    remote_host = models.CharField(max_length=50)
    query_string = models.URLField()
