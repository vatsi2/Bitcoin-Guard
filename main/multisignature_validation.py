def validate_multisig(signatures, pubkeys, tx_hash):
    valid_sigs = 0
    for sig, pubkey in zip(signatures, pubkeys):
        vk = ecdsa.VerifyingKey.from_string(pubkey, curve=ecdsa.SECP256k1)
        if vk.verify(sig, tx_hash, hashfunc=hashlib.sha256):
            valid_sigs += 1
    return valid_sigs >= 2  # 2-of-3
