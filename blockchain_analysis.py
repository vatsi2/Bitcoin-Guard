# Bitcoin whale transaction analysis module
from bitcoinrpc import BitcoinRPC
import pandas as pd

class BlockchainAnalyzer:
    def __init__(self, rpc_user, rpc_password):
        self.rpc = BitcoinRPC(
            user=rpc_user,
            password=rpc_password,
            host='localhost',
            port=8332
        )
        
    def get_whale_transactions(self, min_btc=50):
        """Returns transactions > min_btc BTC"""
        mempool = self.rpc.getrawmempool(True)
        large_txs = []
        
        for txid, tx_info in mempool.items():
            for vout in tx_info['vout']:
                if vout['value'] >= min_btc:
                    large_txs.append({
                        'txid': txid,
                        'amount': vout['value'],
                        'address': vout['scriptPubKey']['addresses'][0]
                    })
                    
        return pd.DataFrame(large_txs)

# Utilization
analyzer = BlockchainAnalyzer('user', 'pass')
whales = analyzer.get_whale_transactions(min_btc=100)
print(f"Обнаружено китовых транзакций: {len(whales)}")
