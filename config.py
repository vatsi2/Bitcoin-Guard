from pydantic import BaseSettings, Field, HttpUrl
from typing import List, Optional


class ExchangeConfig(BaseSettings):
    name: str
    api_key: Optional[str]
    secret: Optional[str]
    rpc_url: Optional[HttpUrl]
    private_key: Optional[str]


class ArbitrageConfig(BaseSettings):
    min_spread_pct: float = Field(0.2, ge=0)
    trade_amount_btc: float = Field(0.1, ge=0)
    cross_chain: bool = True


class TWAPConfig(BaseSettings):
    interval_seconds: int = Field(60, ge=1)
    slices: int = Field(10, ge=1)


class LongShortConfig(BaseSettings):
    max_leverage: int = Field(5, ge=1)
    default_side: str = Field("both", regex="^(long|short|both)$")


class RiskConfig(BaseSettings):
    max_drawdown_pct: float = Field(0.05, ge=0)
    hedge_allocation_pct: float = Field(0.5, ge=0, le=1)


class AlertConfig(BaseSettings):
    email: Optional[str]
    webhook_url: Optional[HttpUrl]


class Settings(BaseSettings):
    exchanges: List[ExchangeConfig]
    arbitrage: ArbitrageConfig = ArbitrageConfig()
    twap: TWAPConfig = TWAPConfig()
    long_short: LongShortConfig = LongShortConfig()
    risk: RiskConfig = RiskConfig()
    alerts: AlertConfig = AlertConfig()
    scheduler_interval_sec: int = Field(5, ge=1)

    class Config:
        env_file = ".env"
        env_nested_delimiter = '__'

settings = Settings()


# exchange_manager.py
import ccxt.async_support as ccxt
import asyncio
from typing import Dict, Any
from logger import get_logger

logger = get_logger("ExchangeManager")


class ExchangeManager:
    def __init__(self, configs: list):
        self.exchanges: Dict[str, ccxt.Exchange] = {}
        for cfg in configs:
            ex_class = getattr(ccxt, cfg.name)
            client = ex_class({
                'apiKey': cfg.api_key,
                'secret': cfg.secret,
                'enableRateLimit': True,
            })
            self.exchanges[cfg.name] = client
            logger.info(f"Initialized {cfg.name}")

    async def fetch_ticker(self, symbol: str) -> Dict[str, float]:
        tasks = [ex.fetch_ticker(symbol) for ex in self.exchanges.values()]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return {name: res['last'] for name, res in zip(self.exchanges.keys(), results) if not isinstance(res, Exception)}

    async def place_order(self, exchange_name: str, symbol: str, side: str, amount: float, price: float = None) -> Any:
        ex = self.exchanges[exchange_name]
        try:
            if price:
                order = await ex.create_limit_order(symbol, side, amount, price)
            else:
                order = await ex.create_market_order(symbol, side, amount)
            logger.info(f"{side.upper()} {amount} {symbol} on {exchange_name} @ {price or 'market'}")
            return order
        except Exception as e:
            logger.error(f"Order error on {exchange_name}: {e}")
            return None

    async def close(self):
        await asyncio.gather(*(ex.close() for ex in self.exchanges.values()))
