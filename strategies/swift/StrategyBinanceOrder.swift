import BinanceKit

let client = BinanceClient(apiKey:"KEY", secret:"SECRET")
client.createOrder(symbol:"BTCUSDT", side:.buy, type:.limit, quantity:"0.01", price:"29000") { result in
    print(result)
}
