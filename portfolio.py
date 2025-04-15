import asyncio
from logger import get_logger

logger = get_logger("Portfolio")

class Portfolio:
    def __init__(self, ex_mgr):
        self.ex_mgr = ex_mgr

    def total_value(self) -> float:
        """
        Aggregate USD value from all exchanges.
        Note: For production, replace synchronous calls with async calls.
        """
        total = 0.0
        for name, client in self.ex_mgr.exchanges.items():
            try:
                balance = client.fetch_balance()  # Synchronous call (for demo purposes)
                usdt = balance.get('USDT', {}).get('free', 0)
                btc = balance.get('BTC', {}).get('free', 0)
                # Fetch ticker synchronously for simplicity; in production, use async
                ticker = asyncio.run(self.ex_mgr.fetch_ticker('BTC/USDT')).get(name, 0)
                total += usdt + btc * ticker
            except Exception as e:
                logger.error(f"Error fetching balance from {name}: {e}")
        return total

    def total_btc(self) -> float:
        """
        Return total BTC holdings.
        """
        total = 0.0
        for name, client in self.ex_mgr.exchanges.items():
            try:
                balance = client.fetch_balance()  # Synchronous call (for demo purposes)
                btc = balance.get('BTC', {}).get('free', 0)
                total += btc
            except Exception as e:
                logger.error(f"Error fetching BTC balance from {name}: {e}")
        return total

    def pending_order_amount(self) -> float:
        """
        Placeholder: Calculate the amount for the next TWAP order.
        """
        return 0.5

    def execute_hedge(self, btc_amount: float):
        """
        Execute a hedge by selling BTC proportionally across exchanges.
        """
        num_exchanges = len(self.ex_mgr.exchanges)
        if num_exchanges == 0:
            logger.error("No exchanges available for hedging!")
            return

        amount_per_ex = btc_amount / num_exchanges
        for ex in self.ex_mgr.exchanges.keys():
            # This is a synchronous placeholder; in production, call async methods.
            from asyncio import run
            run(self.ex_mgr.place_order(ex, 'BTC/USDT', 'sell', amount_per_ex))
        logger.info(f"Executed hedge: sold {btc_amount} BTC across {num_exchanges} exchanges")
