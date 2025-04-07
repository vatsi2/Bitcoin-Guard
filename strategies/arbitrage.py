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
        if not self.risk_mgr.can_trade:
            return
        prices = await self.ex_mgr.fetch_ticker('BTC/USDT')
        sorted_ex = sorted(prices.items(), key=lambda x: x[1])
        buy_ex, buy_price = sorted_ex[0]
        sell_ex, sell_price = sorted_ex[-1]
        spread = (sell_price - buy_price) / buy_price * 100
        if spread >= self.cfg.min_spread_pct:
            amount = self.cfg.trade_amount_btc
            tasks = [
                self.ex_mgr.place_order(buy_ex, 'BTC/USDT', 'buy', amount),
                self.ex_mgr.place_order(sell_ex, 'BTC/USDT', 'sell', amount)
            ]
            await asyncio.gather(*tasks)
            logger.info(f"Arbitrage: {buy_ex}->{sell_ex}, spread={spread:.2f}%")
