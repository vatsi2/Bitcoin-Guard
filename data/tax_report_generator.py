import pandas as pd  
from tax_methods import fifo, lifo  

class TaxEngine:  
    def __init__(self, transactions):  
        self.df = pd.DataFrame(transactions)  
        self.df['date'] = pd.to_datetime(self.df['timestamp'], unit='s')  

    def generate_report(self, method="FIFO"):  
        if method == "FIFO":  
            return fifo.calculate(self.df)  
        elif method == "LIFO":  
            return lifo.calculate(self.df)  
        else:  
            raise ValueError("Unsupported tax method")  

    def export_to_csv(self, path):  
        self.df.to_csv(path, columns=[  
            'date', 'asset', 'amount', 'cost_basis', 'proceeds'  
        ])  

# Usage:  
transactions = [...]  # From blockchain/CEX APIs  
tax_engine = TaxEngine(transactions)  
tax_engine.generate_report(method="FIFO").export_to_csv("tax_2023.csv")  
