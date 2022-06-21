import os
import shutil

from PIL import Image
from web3 import Web3

from eth_api.helpers import calc_hash, get_contract, load_abi_address, TRANSACTION_URL, TRANSACTION_ROOT


def upl_file(path_to_file, description_of_file="description_text", who_ami=0, base_width=300):
    temp_image = os.path.join(TRANSACTION_ROOT, "temp_pic.jpg")
    w3 = Web3(Web3.HTTPProvider(TRANSACTION_URL))

    abi, address = load_abi_address(transaction_name="nft")

    im = Image.open(path_to_file)
    rgb_im = im.convert('RGB')

    w_percent = base_width / rgb_im.size[0]
    hsize = int(rgb_im.size[1] * w_percent)
    img = rgb_im.resize((base_width, hsize), Image.ANTIALIAS)
    img.save(temp_image)

    hash_sha256 = calc_hash(temp_image)
    new_path = os.path.join(TRANSACTION_ROOT, "uploads", f"{hash_sha256}.jpg")
    shutil.copy(temp_image, new_path)

    contract = get_contract(w3, address, abi)

    w3.eth.default_account = w3.eth.accounts[who_ami]
    contract.functions.uploadImage(hash_sha256, description_of_file).transact()
