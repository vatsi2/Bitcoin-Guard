def detect_leverage_cycle(trade_history):
    drawdowns = []
    for trade in trade_history:
        if trade['pnl'] < 0:
            drawdowns.append(trade['pnl_pct'])
        else:
            if len(drawdowns) >= 3:
                return True
            drawdowns = []
    return False
