from ecdsa import SigningKey, SECP256k1

def sign_transaction_offline(unsigned_tx, priv_key):
    sk = SigningKey.from_string(priv_key, curve=SECP256k1)
    signature = sk.sign_deterministic(unsigned_tx, hashfunc=hashlib.sha256)
    return signature.hex()
