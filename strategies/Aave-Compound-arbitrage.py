from web3 import Web3
from aave import Aave
from compound import Compound

def interest_rate_arbitrage():
    aave_rates = Aave.get_deposit_rates()
    compound_rates = Compound.get_borrow_rates()
    
    # If the deposit rate Aave > borrowed Compound
    if aave_rates['USDC'] > compound_rates['USDC'] + 0.02:  # 2% margin
        amount = 1000  # USDC
        # Loan to Compound
        Compound.borrow(amount, 'USDC')
        # Deposit on Aave
        Aave.deposit(amount, 'USDC')
        # Logging
        logger.info(f"Arbitration: +{aave_rates['USDC'] - compound_rates['USDC']}%")
