import hashlib
import json
import os
from datetime import datetime as dt
from pathlib import Path

from dotenv import dotenv_values
from solcx import compile_source

TRANSACTION_ROOT = Path(__file__).resolve().parent

config = dotenv_values(os.path.join(Path(__file__).resolve().parent.parent, ".env"))
TRANSACTION_URL = config['TRANSACTION_URL']


def deploy_contract(w3, sol_name):
    compiled_solidity = compile_source(open(
        os.path.join(TRANSACTION_ROOT, sol_name), 'r').read(),
                                       output_values=['abi', 'bin'])
    contract_id, contract_interface = compiled_solidity.popitem()
    w3.eth.default_account = w3.eth.accounts[0]
    nft = w3.eth.contract(abi=contract_interface['abi'],
                          bytecode=contract_interface['bin'])
    transaction_hash = nft.constructor().transact()
    w3.eth.default_account = w3.eth.accounts[1]
    transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
    address = transaction_receipt.contractAddress,
    abi = contract_interface['abi']
    return address[0], abi


def save_abi_address(transaction_name, abi, address):
    path = os.path.join(TRANSACTION_ROOT, f"{transaction_name}.abi")
    with open(path, "w") as f:
        f.write(json.dumps(abi))

    path = os.path.join(TRANSACTION_ROOT, f"{transaction_name}.address")
    with open(path, "w"):
        f.write(address)
        f.close()


def load_abi_address(transaction_name):
    with open(os.path.join(TRANSACTION_ROOT, f"{transaction_name}.abi"), "r") as f:
        abi = f.read()

    with open(os.path.join(TRANSACTION_ROOT, f"{transaction_name}.address"), "r") as f:
        address = f.read()

    return abi, address


def get_contract(w3, address, abi):
    return w3.eth.contract(address=address, abi=abi)


def show_balances(contract):
    _image_count = contract.functions.imageCount().call()
    for i in range(1, _image_count + 1):
        im_id, im_hash, description, tip_amount, author, timestamp = contract.functions.images(i).call()
        print(im_id, im_hash, description, tip_amount, author, timestamp)


def get_balances(contract):
    _image_count = contract.functions.imageCount().call()
    result = []
    for i in range(1, _image_count + 1):
        keys = ("im_id", "im_hash", "description", "tipAmount", "author", "timestamp")
        vals = contract.functions.images(i).call()
        rez = {k: v for k, v in zip(keys, vals)}
        rez['timestamp'] = dt.utcfromtimestamp(rez['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
        result.append(rez)
    return result


def calc_hash(filename):
    with open(filename, "rb") as f:
        readable_hash = hashlib.sha256(f.read()).hexdigest()
        return readable_hash


def image_count(contract):
    return contract.functions.imageCount().call()
