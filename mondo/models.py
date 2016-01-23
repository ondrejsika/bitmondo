from django.db import models


class MondoAccount(models.Model):
    username = models.CharField(max_length=64)
    token = models.CharField(max_length=256)
    account_id = models.CharField(max_length=64)

    def __unicode__(self):
        return u'%s' % self.username


class BitcoinAddress(models.Model):
    account = models.ForeignKey(MondoAccount)
    address = models.CharField(max_length=40)

    def __unicode__(self):
        return u'%s %s' % (self.account, self.address)
