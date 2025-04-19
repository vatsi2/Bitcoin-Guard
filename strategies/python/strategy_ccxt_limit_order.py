import ccxt  # CCXT unified API :contentReference[oaicite:1]{index=1}

def place_limit_order():
    exchange = ccxt.binance({'apiKey': 'KEY', 'secret': 'SECRET'})
    symbol = 'BTC/USDT'
    type, side, amount, price = 'limit', 'buy', 0.01, 30000
    order = exchange.create_order(symbol, type, side, amount, price)  # create_order unified method :contentReference[oaicite:2]{index=2}
    print(order)
