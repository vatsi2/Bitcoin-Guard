# Technical Analysis Module
import pandas as pd
import talib

class TechnicalAnalyzer:
    def __init__(self, ohlc_data):
        self.df = pd.DataFrame(ohlc_data)
        
    def calculate_indicators(self):
        """Calculation of RSI, MACD, Bollinger Bands"""
        self.df['RSI'] = talib.RSI(self.df['close'], timeperiod=14)
        self.df['MACD'], _, _ = talib.MACD(self.df['close'])
        self.df['upper_band'], self.df['middle_band'], self.df['lower_band'] = \
            talib.BBANDS(self.df['close'], timeperiod=20)
        return self.df

# Utilization
data = {'close': [...]}  # Historical price data
analyzer = TechnicalAnalyzer(data)
analysis = analyzer.calculate_indicators()
print(analysis.tail())
