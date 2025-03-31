def optimal_sell_schedule(total_btc, market_volatility):
    chunks = int(total_btc / (market_volatility * 0.1))
    return total_btc / chunks # размер каждого ордера
