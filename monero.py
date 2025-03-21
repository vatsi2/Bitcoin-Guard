from monero.wallet import Wallet
from monero.backends.jsonrpc import JSONRPCWallet

def monero_transfer(address: str, amount: float):
    wallet = Wallet(JSONRPCWallet(port=28088))
    tx = wallet.transfer(address, amount)
    return tx.hash
