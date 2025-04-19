import com.binance.api.client.BinanceApiClientFactory

fun main() {
    val factory = BinanceApiClientFactory.newInstance("KEY", "SECRET")
    val client = factory.newRestClient()
    client.newOrderTest(NewOrder.limitBuy("BTCUSDT","0.01","29000"))  // test endpoint
}
