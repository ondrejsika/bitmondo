BITCOIN_IMG_URL = 'https://bitstickers.net/wp-content/uploads/2013/12/btc-orange.jpg'

def shorten_address(address, size=6):
    return '%s...%s' % (address[:size], address[-size:])


class BitMondoClient(object):
    def __init__(self, mondo_session, account_id):
        self._mondo_session = mondo_session
        self._account_id = account_id

    def incoming_payment(self, from_address, to_address, amount_btc, tx_id):
        self._mondo_session.create_feed_item(
            self._account_id,
            'Bitcoin tx %s BTC' % amount_btc,
            'from %s to %s' % (shorten_address(from_address), shorten_address(to_address)),
            BITCOIN_IMG_URL,
            'https://blockchain.info/tx/%s' % tx_id,
            '#008000',
            '#000',
            '#FFF',
        )

    def outgoing_payment(self, from_address, to_address, amount_btc, tx_id):
        self._mondo_session.create_feed_item(
            self._account_id,
            'Bitcoin tx %s BTC' % amount_btc,
            'from %s to %s' % (shorten_address(from_address), shorten_address(to_address)),
            BITCOIN_IMG_URL,
            'https://blockchain.info/tx/%s' % tx_id,
            'FF0000',
            '#000',
            '#FFF',
            )
