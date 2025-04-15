This module uses Pydantic to manage and validate configuration settings for Royen.
It reads settings from environment variables and a .env file.
"""

from pydantic import BaseSettings, Field, HttpUrl
from typing import List, Optional


class ExchangeConfig(BaseSettings):
    name: str
    api_key: Optional[str] = None
    secret: Optional[str] = None
    rpc_url: Optional[HttpUrl] = None
    private_key: Optional[str] = None

class ArbitrageConfig(BaseSettings):
    min_spread_pct: float = Field(0.2, description="Minimum spread percentage to trigger arbitrage")
    trade_amount_btc: float = Field(0.1, description="BTC amount per arbitrage cycle")
    cross_chain: bool = Field(True, description="Enable cross-chain arbitrage")

class TWAPConfig(BaseSettings):
    interval_seconds: int = Field(60, description="Interval in seconds between TWAP slices")
    slices: int = Field(10, description="Number of TWAP slices per order")

class LongShortConfig(BaseSettings):
    max_leverage: int = Field(5, description="Maximum leverage for margin/futures positions")
    default_side: str = Field("both", description="Default trading side: long, short, or both", regex="^(long|short|both)$")

class RiskConfig(BaseSettings):
    max_drawdown_pct: float = Field(0.05, description="Maximum allowed drawdown percentage")
    hedge_allocation_pct: float = Field(0.5, description="Percentage of BTC exposure to hedge when drawdown limit is reached")

class AlertConfig(BaseSettings):
    email: Optional[str] = Field(None, description="Email address for sending alerts")
    webhook_url: Optional[HttpUrl] = Field(None, description="Webhook URL for real-time alerts")

class Settings(BaseSettings):
    exchanges: List[ExchangeConfig]
    arbitrage: ArbitrageConfig = ArbitrageConfig()
    twap: TWAPConfig = TWAPConfig()
    long_short: LongShortConfig = LongShortConfig()
    risk: RiskConfig = RiskConfig()
    alerts: AlertConfig = AlertConfig()
    scheduler_interval_sec: int = Field(5, description="Global scheduler loop interval in seconds")

    class Config:
        env_file = ".env"
        env_nested_delimiter = "__"

settings = Settings()
