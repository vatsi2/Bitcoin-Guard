import numpy as np
from arch import arch_model

class GARCHVolatility:
    def __init__(self, returns: np.ndarray):
        self.model = arch_model(returns, vol='Garch', p=1, q=1)
        
    def forecast(self, horizon: int = 1) -> float:
        fit = self.model.fit(disp='off')
        return fit.forecast(horizon=horizon).variance.values[-1, 0] ** 0.5
