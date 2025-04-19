import org.knowm.xchange.Exchange;
import org.knowm.xchange.binance.BinanceExchange;
import org.knowm.xchange.service.trade.TradeService;
import org.knowm.xchange.dto.trade.MarketOrder;
import org.knowm.xchange.currency.CurrencyPair;

public class StrategyBinanceOrder {
    public static void main(String[] args) throws Exception {
        Exchange exchange = new BinanceExchange();
        TradeService trade = exchange.getTradeService();
        MarketOrder order = new MarketOrder.Builder(org.knowm.xchange.dto.Order.OrderType.BID, CurrencyPair.BTC_USDT)
            .originalAmount(org.knowm.xchange.utils.BigDecimalUtils.parse("0.005"))
            .build();
        trade.placeMarketOrder(order);  // XChange library
    }
}
