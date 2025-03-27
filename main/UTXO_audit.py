def audit_utxo(utxo):
    with BlockstreamAPI() as api:
        tx = api.get_transaction(utxo.txid)
        for i, output in enumerate(tx.out):
            if output.script == utxo.script:
                return output.value == utxo.value
    return False
