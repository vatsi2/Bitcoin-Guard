import time
from logger import get_logger
from utils import human_friendly_time

logger = get_logger("PerformanceMonitor")

class PerformanceMonitor:
    def __init__(self):
        self.start_time = time.time()
        self.trade_count = 0

    def log_trade(self):
        """Increment the trade count each time a trade is executed."""
        self.trade_count += 1
        logger.info(f"Trade executed. Total trades so far: {self.trade_count}")

    def generate_report(self, portfolio_value: float):
        """Generate and log a human-friendly performance report."""
        elapsed = time.time() - self.start_time
        report = (
            f"Performance Report:\n"
            f" - Uptime: {human_friendly_time(elapsed)}\n"
            f" - Total Trades Executed: {self.trade_count}\n"
            f" - Current Portfolio Value: ${portfolio_value:,.2f}\n"
        )
        logger.info(report)
        return report
