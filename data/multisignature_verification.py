from bitcoinlib.transactions import Transaction

tx = Transaction.parse_hex(raw_tx)
if tx.verify_signatures(public_keys=['key1', 'key2', 'key3']) >= 3:
    broadcast(tx)
