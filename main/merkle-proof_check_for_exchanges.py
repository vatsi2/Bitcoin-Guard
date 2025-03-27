def verify_merkle_proof(tx_hash, proof, merkle_root):
    current_hash = tx_hash
    for node in proof:
        current_hash = sha256(concat(node, current_hash))
    return current_hash == merkle_root
