using Binance.Net;
using Binance.Net.Enums;
using CryptoExchange.Net.Authentication;

class StrategyBinanceOrder {
    static void Main() {
        var client = new BinanceClient(new BinanceClientOptions {
            ApiCredentials = new ApiCredentials("KEY","SECRET")
        });
        var result = client.Spot.Order.PlaceOrder("BTCUSDT", OrderSide.Buy, SpotOrderType.Limit, 0.01m, price:29000m);
    }
}
