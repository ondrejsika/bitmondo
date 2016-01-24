import requests

def satoshi_to_btc(sat):
    return float(sat) / 10**8


def get_balance(address):
    return requests.get('https://blockchain.info/q/addressbalance/%s' % address).json()


def get_last_tx_id(address):
    raw_address = requests.get('https://blockchain.info/address/%s?format=json&limit=1&offset=0' % address).json()
    return raw_address['txs'][0]['hash']
