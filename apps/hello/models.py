from django.db import models

# Create your models here.
class Contats(models.Model):
    name       = models.CharField(max_length=20)
    surname    = models.CharField(max_length=20)
    dateofbird = models.DateField()
    bio        = models.TextField()
    email    = models.CharField(max_length=20)
    jabber    = models.CharField(max_length=20)
    skype    = models.CharField(max_length=20)
    others      = models.TextField()
    
    def __unicode__(self):
        return self.name
