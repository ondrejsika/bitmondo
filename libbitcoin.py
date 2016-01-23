import requests

def satoshi_to_btc(sat):
    return float(sat) / 10**8


def get_balance(address):
    return requests.get('https://blockchain.info/q/addressbalance/%s' % address).json()

