import datetime
from logger import get_logger

logger = get_logger("Analytics")

class Analytics:
    def __init__(self, portfolio):
        self.portfolio = portfolio
        self.start_time = datetime.datetime.now()
        self.trade_logs = []

    def log_trade(self, trade_info: dict):
        trade_info['timestamp'] = datetime.datetime.now().isoformat()
        self.trade_logs.append(trade_info)
        logger.info(f"Trade logged: {trade_info}")

    def generate_report(self):
        duration = datetime.datetime.now() - self.start_time
        total_value = self.portfolio.total_value()
        report = {
            'duration': str(duration),
            'portfolio_value': total_value,
            'number_of_trades': len(self.trade_logs),
            'trade_logs': self.trade_logs
        }
        logger.info(f"Generated Performance Report: {report}")
        return report
