import ccxt.async_support as ccxt
import asyncio
from typing import Dict, Any
from logger import get_logger

logger = get_logger("ExchangeManager")

class ExchangeManager:
    def __init__(self, exchange_configs: list):
        self.exchanges: Dict[str, Any] = {}
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
                # Simulated DEX client using dummy implementation
                self.exchanges[cfg.name] = DummyDEXClient(cfg.rpc_url, cfg.private_key)
                logger.info(f"Initialized DEX client: {cfg.name}")
            else:
                logger.warning(f"Configuration incomplete for {cfg.name}; skipping.")

    async def fetch_ticker(self, symbol: str) -> Dict[str, float]:
        tasks = [ex.fetch_ticker(symbol) for ex in self.exchanges.values()]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        ticker_data = {}
        for name, res in zip(self.exchanges.keys(), results):
            if isinstance(res, Exception):
                logger.error(f"Error fetching ticker from {name}: {res}")
            else:
                ticker_data[name] = res.get('last', 0.0)
        return ticker_data

    async def place_order(self, exchange_name: str, symbol: str, side: str, amount: float, price: float = None) -> Any:
        ex = self.exchanges.get(exchange_name)
        if not ex:
            logger.error(f"Exchange {exchange_name} not found!")
            return None
        try:
            if price:
                order = await ex.create_limit_order(symbol, side, amount, price)
            else:
                order = await ex.create_market_order(symbol, side, amount)
            logger.info(f"Order placed: {side.upper()} {amount} {symbol} on {exchange_name} at {price or 'market'}")
            return order
        except Exception as e:
            logger.error(f"Order error on {exchange_name}: {e}")
            return None

    async def close(self):
        tasks = [ex.close() for ex in self.exchanges.values() if hasattr(ex, "close")]
        await asyncio.gather(*tasks)

# Dummy DEX client to simulate DEX behavior using Web3.py-like operations
class DummyDEXClient:
    def __init__(self, rpc_url: str, private_key: str):
        self.rpc_url = rpc_url
        self.private_key = private_key

    async def fetch_ticker(self, symbol: str) -> Dict[str, float]:
        return {'last': 30000.0}  # Simulated price

    async def create_market_order(self, symbol: str, side: str, amount: float) -> Dict[str, Any]:
        return {'id': 'dummy_market_order', 'symbol': symbol, 'side': side, 'amount': amount}

    async def create_limit_order(self, symbol: str, side: str, amount: float, price: float) -> Dict[str, Any]:
        return {'id': 'dummy_limit_order', 'symbol': symbol, 'side': side, 'amount': amount, 'price': price}

    async def close(self):
        pass
