# risk_analyzer.py
from pythclient import PythClient
import pandas as pd

class RiskEngine:
    def __init__(self, config):
        self.pyth = PythClient(config['pyth_endpoint'])
        self.max_exposure = config['max_rwa_exposure']
    
    def calculate_rwa_risk(self, portfolio: pd.DataFrame) -> dict:
        rwa_assets = self.pyth.get_rwa_list()
        exposure = portfolio[portfolio['asset'].isin(rwa_assets)]['value'].sum()
        
        return {
            "rwa_exposure": exposure / portfolio['total_value'],
            "recommendation": "Hedge using Mirror Protocol" 
                if exposure > self.max_exposure else None
        }

    def auto_hedge(self, portfolio):
        risk_report = self.calculate_rwa_risk(portfolio)
        
        if risk_report['rwa_exposure'] > self.max_exposure:
            amount = (risk_report['rwa_exposure'] - self.max_exposure) * portfolio['total_value']
            self.execute_hedge(amount)
