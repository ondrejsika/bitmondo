from libbitcoin import get_balance, get_last_tx

from mondo.models import MondoAccount


def cron():
    for account in MondoAccount.objects.all():
        for address in account.bitcoinaddress_set.all():
            balance = get_balance(address.address)
            if address.last_balance != balance:
                last_tx = get_last_tx(address.address)
                address.send_notification(balance, last_tx)
                address.last_balance = balance
                address.save()

