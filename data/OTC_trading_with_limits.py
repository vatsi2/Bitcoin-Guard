def execute_otc_trade(btc_amount, daily_limit=5.0):
    if btc_amount > daily_limit:
        raise Exception("Daily limit exceeded")
    # Binance OTC API call
    binance_otc.execute(order)
