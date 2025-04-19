import ccxt.async_support as ccxt  # Async CCXT :contentReference[oaicite:3]{index=3}

async def place_margin_order():
    binance = ccxt.binance({'apiKey': 'KEY', 'secret': 'SECRET'})
    await binance.load_markets()
    order = await binance.create_order('BTC/USDT', 'limit', 'sell', 0.005, 31000, {'type': 'margin'})  # margin param :contentReference[oaicite:4]{index=4}
    print(order)
    await binance.close()
