import asyncio
from config import settings
from logger import get_logger

logger = get_logger("ArbitrageStrategy")

class ArbitrageStrategy:
    def __init__(self, ex_mgr, portfolio, risk_mgr):
        self.ex_mgr = ex_mgr
        self.portfolio = portfolio
        self.risk_mgr = risk_mgr
        self.cfg = settings.arbitrage

    async def run(self):
        """
        Monitor market spreads and execute arbitrage orders when conditions are met.
        """
        if not self.risk_mgr.can_trade:
            return

        prices = await self.ex_mgr.fetch_ticker('BTC/USDT')
        if not prices:
            logger.error("No ticker data available for arbitrage.")
            return

        # Find best buy (lowest price) and best sell (highest price)
        sorted_prices = sorted(prices.items(), key=lambda item: item[1])
        buy_ex, buy_price = sorted_prices[0]
        sell_ex, sell_price = sorted_prices[-1]
        spread = ((sell_price - buy_price) / buy_price) * 100

        if spread >= self.cfg.min_spread_pct:
            trade_amount = self.cfg.trade_amount_btc
            tasks = [
                self.ex_mgr.place_order(buy_ex, 'BTC/USDT', 'buy', trade_amount),
                self.ex_mgr.place_order(sell_ex, 'BTC/USDT', 'sell', trade_amount),
            ]
            await asyncio.gather(*tasks)
            logger.info(f"Arbitrage executed: Buy on {buy_ex} at {buy_price}, Sell on {sell_ex} at {sell_price} (Spread: {spread:.2f}%)")
