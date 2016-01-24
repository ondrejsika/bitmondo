import requests

def satoshi_to_btc(sat):
    return float(sat) / 10**8


def get_balance(address):
    return requests.get('https://blockchain.info/q/addressbalance/%s' % address).json()


def get_last_tx(address):
    """
    Retruns 5-tuple of (tx_hash, address_from, address_from_count, address_to, address_to_count)
    """
    raw_address = requests.get('https://blockchain.info/address/%s?format=json&limit=1&offset=0' % address).json()

    inputs = raw_address['txs'][0]['inputs']
    address_from_count = len(inputs)
    try:
        address_from = inputs[0]['prev_out'][0]['addr']
    except KeyError:
        address_from = 'NEW COINS'

    outputs = raw_address['txs'][0]['out']
    address_to_count = len(outputs)
    if outputs:
        address_to = outputs[0]['addr']
        for out in outputs:
            if out['addr'] == address:
                address_to = address

    return raw_address['txs'][0]['hash'], address_from, address_from_count, address_to, address_to_count
