require 'binance'

client = Binance::Client::REST.new(api_key: 'KEY', secret_key: 'SECRET')
client.create_order(symbol: 'BTCUSDT', side: 'BUY', type: 'LIMIT', quantity: 0.01, price: 29000) 
