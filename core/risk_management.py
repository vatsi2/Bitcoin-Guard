class RiskEngine:
    @staticmethod
    def check_position_risk(exposure: float, total_capital: float) -> bool:
        return exposure / total_capital <= 0.05  # 5% max per position

    @staticmethod
    def circuit_breaker(loss_threshold: float = 0.1):
        """Halt trading after 10% daily drawdown"""
        current_loss = PortfolioCalculator.get_daily_pnl()
        if current_loss < -abs(loss_threshold):
            raise TradingHaltedError("Circuit breaker triggered")
