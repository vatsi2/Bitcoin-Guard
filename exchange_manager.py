import ccxt.async_support as ccxt
import asyncio
from typing import Dict, Any
from logger import get_logger

logger = get_logger("ExchangeManager")


class ExchangeManager:
    def __init__(self, exchange_configs: list):
        """
        Initialize exchanges based on configuration.
        """
        self.exchanges: Dict[str, ccxt.Exchange] = {}
        for cfg in exchange_configs:
            if cfg.api_key and cfg.secret:
                # Initialize a centralized exchange client
                ex_class = getattr(ccxt, cfg.name)
                client = ex_class({
                    'apiKey': cfg.api_key,
                    'secret': cfg.secret,
                    'enableRateLimit': True,
                })
                self.exchanges[cfg.name] = client
                logger.info(f"Initialized CEX client: {cfg.name}")
            elif cfg.rpc_url and cfg.private_key:
                # For DEX, you might implement a similar client using Web3.py here.
                # For the sake of this example, we'll simulate a DEX client.
                self.exchanges[cfg.name] = DummyDEXClient(cfg.rpc_url, cfg.private_key)
                logger.info(f"Initialized DEX client: {cfg.name}")
            else:
                logger.warning(f"Incomplete configuration for {cfg.name}, skipping initialization.")

    async def fetch_ticker(self, symbol: str) -> Dict[str, float]:
        """
        Fetch the latest ticker information from all configured exchanges.
        """
        tasks = []
        for ex in self.exchanges.values():
            tasks.append(ex.fetch_ticker(symbol))
        results = await asyncio.gather(*tasks, return_exceptions=True)
        ticker_data = {}
        for name, res in zip(self.exchanges.keys(), results):
            if isinstance(res, Exception):
                logger.error(f"Error fetching ticker from {name}: {res}")
            else:
                ticker_data[name] = res.get('last')
        return ticker_data

    async def place_order(self, exchange_name: str, symbol: str, side: str, amount: float, price: float = None) -> Any:
        """
        Place an order on a specific exchange.
        """
        ex = self.exchanges.get(exchange_name)
        if not ex:
            logger.error(f"Exchange {exchange_name} not found!")
            return None

        try:
            if price:
                order = await ex.create_limit_order(symbol, side, amount, price)
            else:
                order = await ex.create_market_order(symbol, side, amount)
            logger.info(f"Placed {side.upper()} order for {amount} {symbol} on {exchange_name} at {price or 'market'}")
            return order
        except Exception as e:
            logger.error(f"Error placing order on {exchange_name}: {e}")
            return None

    async def close(self):
        """
        Close all exchange connections gracefully.
        """
        tasks = [ex.close() for ex in self.exchanges.values() if hasattr(ex, "close")]
        await asyncio.gather(*tasks)


# DummyDEXClient to simulate a DEX client using Web3.py
class DummyDEXClient:
    def __init__(self, rpc_url: str, private_key: str):
        self.rpc_url = rpc_url
        self.private_key = private_key

    async def fetch_ticker(self, symbol: str) -> Dict[str, Any]:
        # Simulate fetching ticker data from a DEX.
        return {'last': 30000.0}

    async def create_market_order(self, symbol: str, side: str, amount: float) -> Dict[str, Any]:
        # Simulate sending a transaction to a DEX.
        return {'id': 'dummy_order_market', 'symbol': symbol, 'side': side, 'amount': amount}

    async def create_limit_order(self, symbol: str, side: str, amount: float, price: float) -> Dict[str, Any]:
        # Simulate sending a limit order to a DEX.
        return {'id': 'dummy_order_limit', 'symbol': symbol, 'side': side, 'amount': amount, 'price': price}

    async def close(self):
        # Simulate closing a DEX connection.
        pass
