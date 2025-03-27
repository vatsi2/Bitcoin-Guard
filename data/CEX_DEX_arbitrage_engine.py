import ccxt  
from web3 import Web3  

class ArbitrageBot:  
    def __init__(self, cex_api, dex_rpc):  
        self.binance = ccxt.binance(cex_api)  
        self.thorchain = Web3(Web3.HTTPProvider(dex_rpc))  

    def find_opportunities(self):  
        cex_price = self.binance.fetch_ticker('BTC/USDT')['bid']  
        dex_price = self.thorchain.eth.get_price('BTC', 'USDT')  
        spread = (dex_price - cex_price) / cex_price * 100  
        return spread if spread > 0.5 else None  

    def execute_trade(self, amount):  
        if spread := self.find_opportunities():  
            # Buy on CEX, sell on DEX  
            self.binance.create_market_buy_order('BTC/USDT', amount)  
            self.thorchain.swap(  
                from_asset="USDT",  
                to_asset="BTC",  
                amount=amount,  
                slippage=0.5  
            )  
            return True  
        return False  
