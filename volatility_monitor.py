import ccxt
from statsmodels.tsa.stattools import adfuller

class VolatilityEngine:
    def __init__(self, exchange: str, symbols: list):
        self.exchange = getattr(ccxt, exchange)()
        self.symbols = symbols
    
    def calculate_volatility(self, window=14):
        data = self.exchange.fetch_ohlcv(self.symbols[0], '1h', limit=window)
        closes = [x[4] for x in data]
        return np.std(closes) / np.mean(closes)
