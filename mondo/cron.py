from libbitcoin import get_balance, get_last_tx_id

from mondo.models import MondoAccount


def cron():
    for account in MondoAccount.objects.all():
        for address in account.bitcoinaddress_set.all():
            balance = get_balance(address.address)
            if address.last_balance != balance:
                tx_id = get_last_tx_id(address.address)
                address.send_notification(balance, tx_id)
                address.last_balance = balance
                address.save()

