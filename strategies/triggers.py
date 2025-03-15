# Opening a long position if ETH exceeds SMA(50)
if current_price > sma_50:
    open_position("ETH/USD", "long", 0.1)  # 0.1 ETH
