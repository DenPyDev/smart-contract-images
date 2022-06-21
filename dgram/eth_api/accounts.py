from web3 import Web3

from eth_api.helpers import TRANSACTION_URL


def get_accounts_balances():
    w3 = Web3(Web3.HTTPProvider(TRANSACTION_URL))
    w3.isConnected()
    return [[acc, w3.eth.get_balance(acc)] for acc in w3.eth.accounts]


def get_account_balance(accounts):
    w3 = Web3(Web3.HTTPProvider(TRANSACTION_URL))
    w3.isConnected()
    return w3.eth.get_balance(accounts)


def get_accounts():
    w3 = Web3(Web3.HTTPProvider(TRANSACTION_URL))
    w3.isConnected()
    return w3.eth.accounts
