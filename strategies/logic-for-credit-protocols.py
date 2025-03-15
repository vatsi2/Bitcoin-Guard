if aave.get_ltv() > 0.75:
    top_up_collateral("ETH", 0.1)  # Add 0.1 ETH
