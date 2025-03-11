import numpy as np
from scipy.stats import norm

class VolatilityAdjustedStopLoss:
    def __init__(self, confidence_level=0.95):
        self.confidence = confidence_level
    
    def calculate_dynamic_sl(self, entry_price, volatility):
        z_score = norm.ppf(self.confidence)
        return entry_price * (1 - z_score * volatility * np.sqrt(1/365))
