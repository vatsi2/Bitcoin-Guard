from config import settings
from logger import get_logger

logger = get_logger("LongShortStrategy")


class LongShortStrategy:
    def __init__(self, ex_mgr, portfolio, risk_mgr):
        self.ex_mgr = ex_mgr
        self.portfolio = portfolio
        self.risk_mgr = risk_mgr
        self.cfg = settings.long_short

    async def run(self):
        # Placeholder: implement signal-based entry/exit
        side = self.cfg.default_side
        if side in ('long', 'both'):
            await self.ex_mgr.place_order('binance', 'BTC/USDT', 'buy', 0.01)
            logger.info("Opened long position @ 0.01 BTC")
        if side in ('short', 'both'):
            await self.ex_mgr.place_order('binance', 'BTC/USDT', 'sell', 0.01)
            logger.info("Opened short position @ 0.01 BTC")
