def detect_whale_transactions(tx_volume):
    return [tx for tx in mempool if tx['value'] > 1000] # BTC
