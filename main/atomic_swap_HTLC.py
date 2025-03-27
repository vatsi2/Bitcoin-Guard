# Contract for BTC/XMR atomic swap
contract_script = f"""
OP_IF
    OP_SHA256 {hash_secret} OP_EQUALVERIFY 
    OP_DUP OP_HASH160 {seller_pubkey_hash}
OP_ELSE
    {locktime} OP_CHECKLOCKTIMEVERIFY OP_DROP
    OP_DUP OP_HASH160 {buyer_pubkey_hash}
OP_ENDIF
OP_EQUALVERIFY
OP_CHECKSIG
"""
