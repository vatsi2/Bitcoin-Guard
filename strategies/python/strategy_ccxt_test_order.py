import ccxt  # CCXT unified API

def test_order():
    exchange = ccxt.binance({'apiKey':'KEY','secret':'SECRET'})
    # 'test': True validates without placing real order :contentReference[oaicite:5]{index=5}
    order = exchange.create_order('ETH/BTC','limit','sell',0.1,0.060,'',{ 'test': True })
    print(order)
