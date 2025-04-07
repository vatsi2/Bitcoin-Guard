import asyncio
from config import settings
from strategies.arbitrage import ArbitrageStrategy
from strategies.twap import TWAPStrategy
from strategies.long_short import LongShortStrategy
from risk_manager import RiskManager
from portfolio import Portfolio
from exchange_manager import ExchangeManager


class Scheduler:
    def __init__(self):
        self.ex_mgr = ExchangeManager(settings.exchanges)
        self.portfolio = Portfolio(self.ex_mgr)
        self.risk_mgr = RiskManager(self.portfolio)
        self.arb = ArbitrageStrategy(self.ex_mgr, self.portfolio, self.risk_mgr)
        self.twap = TWAPStrategy(self.ex_mgr, self.portfolio, self.risk_mgr)
        self.ls = LongShortStrategy(self.ex_mgr, self.portfolio, self.risk_mgr)

    async def start(self):
        while True:
            await asyncio.gather(
                self.arb.run(),
                self.twap.run(),
                self.ls.run(),
            )
            self.risk_mgr.monitor()
            await asyncio.sleep(settings.scheduler_interval_sec)
