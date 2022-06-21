from web3 import Web3

from eth_api.helpers import deploy_contract, save_abi_address, TRANSACTION_URL

w3 = Web3(Web3.HTTPProvider(TRANSACTION_URL))
w3.isConnected()

address, abi = deploy_contract(w3, sol_name='Contract.sol')

save_abi_address(transaction_name="nft", abi=abi, address=address)
