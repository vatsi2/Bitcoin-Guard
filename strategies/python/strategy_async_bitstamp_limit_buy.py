import asyncio, ccxt.async_support as ccxt

async def place_bitstamp_buy():
    exchange = ccxt.bitstamp({'apiKey':'KEY','secret':'SECRET'})
    await exchange.load_markets()
    order = await exchange.create_limit_buy_order('BTC/USD', 0.02, 60000)  # async limit buy :contentReference[oaicite:6]{index=6}
    print(order)
    await exchange.close()

asyncio.run(place_bitstamp_buy())
