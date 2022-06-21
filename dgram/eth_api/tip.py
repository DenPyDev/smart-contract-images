from web3 import Web3

from eth_api.helpers import get_contract, load_abi_address, show_balances, TRANSACTION_URL


def tip(imd_n=0, value=123, who_ami=0):
    who_ami = int(who_ami)
    imd_n = int(imd_n)
    value = int(value)

    w3 = Web3(Web3.HTTPProvider(TRANSACTION_URL))
    w3.isConnected()

    abi, address = load_abi_address(transaction_name="nft")

    contract = get_contract(w3, address, abi)

    show_balances(contract)
    w3.eth.default_account = w3.eth.accounts[who_ami]

    transaction = contract.functions.tipImageOwner(imd_n).buildTransaction({
        "gasPrice": w3.eth.gas_price,
        "value": value})

    w3.eth.send_transaction(transaction)
    show_balances(contract)
