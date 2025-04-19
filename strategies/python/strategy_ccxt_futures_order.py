from ccxt import binanceusdm  # USDM futures client :contentReference[oaicite:7]{index=7}

client = binanceusdm({'apiKey':'KEY','secret':'SECRET'})
client.options['defaultType'] = 'future'
order = client.create_order('BTC/USDT:USDT','market','buy',0.001)  # futures market order
print(order)
