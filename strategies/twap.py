import asyncio
from config import settings
from logger import get_logger

logger = get_logger("TWAPStrategy")

class TWAPStrategy:
    def __init__(self, ex_mgr, portfolio, risk_mgr):
        self.ex_mgr = ex_mgr
        self.portfolio = portfolio
        self.risk_mgr = risk_mgr
        self.cfg = settings.twap

    async def run(self):
        """
        Execute TWAP by slicing a large order into multiple smaller orders.
        """
        if not self.risk_mgr.can_trade:
            return

        total_order = self.portfolio.pending_order_amount()
        slice_amount = total_order / self.cfg.slices
        for i in range(self.cfg.slices):
            if not self.risk_mgr.can_trade:
                break
            await self.ex_mgr.place_order('binance', 'BTC/USDT', 'buy', slice_amount)
            logger.info(f"TWAP slice {i+1}/{self.cfg.slices} executed.")
            await asyncio.sleep(self.cfg.interval_seconds)
