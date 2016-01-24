from django.db import models
from django.conf import settings

from libbitmondo import BitMondoClient
from libmondo import MondoSessionClient, MondoOauthClient
from libbitcoin import satoshi_to_btc


mondo_client = MondoOauthClient(
    settings.MONDO_AUTH_URL,
    settings.MONDO_API_URL,
    settings.MONDO_CLIENT_ID,
    settings.MONDO_CLIENT_SECRET,
    settings.MONDO_REDIRECT_URL,
)


class MondoAccount(models.Model):
    username = models.CharField(max_length=64)
    token = models.CharField(max_length=256)
    account_id = models.CharField(max_length=64)

    def __unicode__(self):
        return u'%s' % self.username


class BitcoinAddress(models.Model):
    account = models.ForeignKey(MondoAccount)
    address = models.CharField(max_length=40)
    last_balance = models.IntegerField()

    def __unicode__(self):
        return u'%s %s %s' % (self.account, self.address, self.last_balance)

    def send_notification(self, balance, tx_id):
        change = satoshi_to_btc(balance - self.last_balance)
        mondo_session = MondoSessionClient(mondo_client, self.account.token)
        bitmondo = BitMondoClient(mondo_session, self.account.account_id)
        if change > 0:
            bitmondo.incoming_payment(change, self.address, tx_id)
        else:
            bitmondo.outgoing_payment(-change, self.address, tx_id)
