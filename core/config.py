from pydantic import BaseModel, SecretStr
from typing import Optional

class Settings(BaseModel):
    hyperliquid_api: SecretStr
    aave_rpc: str
    max_risk_per_trade: float = 0.02
    allowed_slippage: float = 0.005
    chain_id: int = 1  # Mainnet
    
    @classmethod
    def load(cls):
        return cls(
            hyperliquid_api=os.getenv("HYPERLIQUID_API_KEY"),
            aave_rpc=os.getenv("AAVE_RPC_URL")
        )
