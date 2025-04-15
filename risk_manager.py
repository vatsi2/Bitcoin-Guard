from logger import get_logger

logger = get_logger("RiskManager")

class RiskManager:
    def __init__(self, portfolio, risk_cfg):
        self.portfolio = portfolio
        self.cfg = risk_cfg
        self.peak_value = self.portfolio.total_value()
        self.can_trade = True

    def monitor(self):
        """
        Check the portfolio value and trigger hedging if drawdown exceeds threshold.
        """
        current_value = self.portfolio.total_value()
        drawdown = (self.peak_value - current_value) / self.peak_value
        if drawdown >= self.cfg.max_drawdown_pct and self.can_trade:
            self._hedge()
        if current_value > self.peak_value:
            self.peak_value = current_value

    def _hedge(self):
        """
        Hedge a portion of BTC to protect the portfolio.
        """
        total_btc = self.portfolio.total_btc()
        hedge_amount = total_btc * self.cfg.hedge_allocation_pct
        self.portfolio.execute_hedge(hedge_amount)
        self.can_trade = False
        logger.warning(f"Hedging triggered! Hedged {hedge_amount} BTC")
