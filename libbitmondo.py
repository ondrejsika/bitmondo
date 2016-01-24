BITCOIN_IMG_URL = 'https://bitstickers.net/wp-content/uploads/2013/12/btc-orange.jpg'

def shorten_address(address, size=6):
    if address == 'NEW COINS':
        return address
    return '%s...%s' % (address[:size], address[-size:])

def from_to_bar(last_tx):
    _, address_from, address_from_count, address_to, address_to_count = last_tx
    out = []
    out.append('from %s' % shorten_address(address_from))
    if address_from_count > 1:
        out.append('+%s' % (address_from_count -1))
    out.append('to %s' % shorten_address(address_to))
    if address_from_count > 1:
        out.append('+%s' % (address_to_count - 1))
    print ' '.join(out)
    return ' '.join(out)

class BitMondoClient(object):
    def __init__(self, mondo_session, account_id):
        self._mondo_session = mondo_session
        self._account_id = account_id

    def incoming_payment(self, amount_btc, last_tx):
        self._mondo_session.create_feed_item(
            self._account_id,
            'Bitcoin tx %.2f BTC' % amount_btc,
            from_to_bar(last_tx),
            BITCOIN_IMG_URL,
            'https://blockchain.info/tx/%s' % last_tx[0],
            '#008000',
            '#000',
            '#FFF',
        )

    def outgoing_payment(self, amount_btc, last_tx):
        self._mondo_session.create_feed_item(
            self._account_id,
            'Bitcoin tx %.2f BTC' % amount_btc,
            from_to_bar(last_tx),
            BITCOIN_IMG_URL,
            'https://blockchain.info/tx/%s' % last_tx[0],
            'FF0000',
            '#000',
            '#FFF',
        )
