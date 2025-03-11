def execute_protection_measures(position):
    if position.unrealized_pnl < -position.max_acceptable_loss:
        # 1. Hedging through perpetual futures
        hedge_with_perps(position.asset)
        
        # 2. Partial closing of the position
        close_percentage = abs(position.unrealized_pnl) / position.max_acceptable_loss
        exchange.close_position(position.id, close_percentage)
        
        # 3. Reallocation of collateral
        collateral_manager.rebalance_collateral()
        
        # 4. Sending a notification to Telegram
        send_alert(f"Emergency measures activated for {position.asset}")
