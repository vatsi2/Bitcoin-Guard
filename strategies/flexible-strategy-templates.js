{
  "strategy": "TrendFollowing",
  "params": {
    "entry_condition": "price > SMA(50)",
    "exit_condition": "price < SMA(20) || stop_loss_triggered",
    "risk_per_trade": 2  // 2% capital per transaction
  }
}
