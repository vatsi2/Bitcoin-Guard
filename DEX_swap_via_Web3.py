# Interaction module with Uniswap
from web3 import Web3
from eth_account import Account

class UniswapSwapper:
    def __init__(self, private_key, rpc_url):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.account = Account.from_key(private_key)
        
    def swap_eth_to_token(self, token_address, amount_eth):
        """ETH token exchange via Uniswap Router v3"""
        router_address = '0xE592427A0AEce92De3Edee1F18E0157C05861564'
        abi = [...]  # ABI Uniswap Router
        
        router = self.w3.eth.contract(address=router_address, abi=abi)
        deadline = int(time.time()) + 1200
        
        tx = router.functions.exactInputSingle({
            'tokenIn': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2', # WETH
            'tokenOut': token_address,
            'fee': 3000,  # 0.3%
            'recipient': self.account.address,
            'deadline': deadline,
            'amountIn': self.w3.to_wei(amount_eth, 'ether'),
            'amountOutMinimum': 0,
            'sqrtPriceLimitX96': 0
        }).build_transaction({
            'from': self.account.address,
            'nonce': self.w3.eth.get_transaction_count(self.account.address),
            'gas': 250000,
            'gasPrice': self.w3.eth.gas_price
        })
        
        signed_tx = self.account.sign_transaction(tx)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()

# Utilization
swapper = UniswapSwapper('PRIVATE_KEY', 'https://mainnet.infura.io/v3/YOUR_ID')
tx_hash = swapper.swap_eth_to_token('0x...DAI', 0.5)
print(f"Транзакция отправлена: {tx_hash}")
