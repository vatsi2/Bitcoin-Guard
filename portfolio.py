import asyncio
from typing import Dict
from logger import get_logger

logger = get_logger("Portfolio")


class Portfolio:
    def __init__(self, ex_mgr):
        self.ex_mgr = ex_mgr

    def total_value(self) -> float:
        # Simplified: fetch balances synchronously
        # Replace with async as needed
        balances = {ex: client.fetch_balance() for ex, client in self.ex_mgr.exchanges.items()}
        # compute total
        total = 0
        for name, bal in balances.items():
            usdt = bal.get('USDT', 0)
            btc = bal.get('BTC', 0)
            price = asyncio.run(self.ex_mgr.fetch_ticker('BTC/USDT')).get(name, 0)
            total += usdt + btc * price
        return total

    def total_btc(self) -> float:
        balances = {ex: client.fetch_balance() for ex, client in self.ex_mgr.exchanges.items()}
        return sum(bal.get('BTC', 0) for bal in balances.values())

    def pending_order_amount(self) -> float:
        # Define based on signal or config
        return 0.5

    def execute_hedge(self, btc_amount: float):
        for ex in self.ex_mgr.exchanges:
            asyncio.run(self.ex_mgr.place_order(ex, 'BTC/USDT', 'sell', btc_amount/len(self.ex_mgr.exchanges)))
        logger.info("Executed hedge across all exchanges")
