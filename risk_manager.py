from config import settings
from logger import get_logger

logger = get_logger("RiskManager")


class RiskManager:
    def __init__(self, portfolio):
        self.portfolio = portfolio
        self.peak = portfolio.total_value()
        self.cfg = settings.risk
        self._can_trade = True

    @property
    def can_trade(self) -> bool:
        return self._can_trade

    def monitor(self):
        current = self.portfolio.total_value()
        drawdown = (self.peak - current) / self.peak
        if drawdown >= self.cfg.max_drawdown_pct and self._can_trade:
            self._hedge()
        if current > self.peak:
            self.peak = current

    def _hedge(self):
        amount = self.portfolio.total_btc() * self.cfg.hedge_allocation_pct
        self.portfolio.execute_hedge(amount)
        self._can_trade = False
        logger.warning(f"Hedged {amount} BTC ({self.cfg.hedge_allocation_pct*100:.1f}% exposure)")
