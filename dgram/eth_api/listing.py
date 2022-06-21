from web3 import Web3

from eth_api.helpers import get_contract, load_abi_address, get_balances, image_count, TRANSACTION_URL


def get_list():
    w3 = Web3(Web3.HTTPProvider(TRANSACTION_URL))
    w3.isConnected()
    abi, address = load_abi_address(transaction_name="nft")
    contract = get_contract(w3, address, abi)
    return get_balances(contract)


def image_counter():
    w3 = Web3(Web3.HTTPProvider(TRANSACTION_URL))
    w3.isConnected()
    abi, address = load_abi_address(transaction_name="nft")
    contract = get_contract(w3, address, abi)
    return image_count(contract=contract)
