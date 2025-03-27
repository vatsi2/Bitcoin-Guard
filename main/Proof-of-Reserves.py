def verify_proof_of_reserves(merkle_root, user_leaf):
    # Binance-style proof validation
    path = user_leaf['path']
    current_hash = sha256(user_leaf['data'])
    for node in path:
        current_hash = sha256(node + current_hash)
    return current_hash == merkle_root
