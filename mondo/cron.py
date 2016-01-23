from libbitcoin import get_balance

from mondo.models import MondoAccount


def cron():
    for account in MondoAccount.objects.all():
        for address in account.bitcoinaddress_set.all():
            balance = get_balance(address.address)
            if address.last_balance != balance:
                address.send_notification(balance)
                address.last_balance = balance
                address.save()

