BITCOIN_IMG_URL = 'https://bitstickers.net/wp-content/uploads/2013/12/btc-orange.jpg'


def shorten_address(address, size=6):
    if len(address) < 2*size+3:
        return address
    return '%s...%s' % (address[:size], address[-size:])


class BitMondoClient(object):
    def __init__(self, mondo_session, account_id):
        self._mondo_session = mondo_session
        self._account_id = account_id

    def incoming_payment(self, amount_btc, address, tx_id):
        self._mondo_session.create_feed_item(
            self._account_id,
            'Bitcoin tx %.4f BTC' % amount_btc,
            'to %s' % shorten_address(address, 14),
            BITCOIN_IMG_URL,
            'https://blockchain.info/tx/%s' % tx_id,
            '#008000',
            '#000',
            '#FFF',
        )

    def outgoing_payment(self, amount_btc, address, tx_id):
        self._mondo_session.create_feed_item(
            self._account_id,
            'Bitcoin tx %.4f BTC' % amount_btc,
            'from %s' % shorten_address(address, 14),
            BITCOIN_IMG_URL,
            'https://blockchain.info/tx/%s' % tx_id,
            'FF0000',
            '#000',
            '#FFF',
        )
