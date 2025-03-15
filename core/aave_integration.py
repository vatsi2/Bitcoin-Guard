from web3 import Web3
from web3.middleware import geth_poa_middleware

class AaveManager:
    def __init__(self, rpc_url: str):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
    def safe_health_factor_update(self, min_hf: float = 1.5):
        current_hf = self.get_health_factor()
        if current_hf < min_hf:
            self.rebalance_collateral()
