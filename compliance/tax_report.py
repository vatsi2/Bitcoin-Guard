from defiguard import FIFOAnalyzer, TaxLotTracker

class CapitalGainsReport:
    def __init__(self, wallet: str, jurisdiction: str):
        self.tracker = TaxLotTracker(wallet)
        self.analyzer = FIFOAnalyzer(jurisdiction)
        
    def generate_report(self) -> pd.DataFrame:
        return self.analyzer.process(self.tracker.transactions)
