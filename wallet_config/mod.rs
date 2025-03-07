// src/signer/mod.rs

pub enum WalletProvider {
    Ledger(HDPath),
    Trezor(Network),
    MetaMask(Url),
    TrustWallet(Chain),
    Fireblocks(ApiKey),
    GnosisSafe(SafeAddress),
}

impl WalletProvider {
    pub async fn sign_transaction(&self, tx: Transaction) -> Result<Signature> {
        match self {
            Self::Ledger(path) => {
                let transport = TransportLedger::new(path.clone())?;
                transport.sign(tx).await
            }
            Self::MetaMask(rpc) => {
                let provider = JsonRpcClient::new(rpc.clone());
                let signer = MetaMaskSigner::new(provider);
                signer.sign(tx).await
            }
            Self::Fireblocks(api_key) => {
                let client = FireblocksClient::new(api_key);
                client.approve_and_sign(tx).await
            }
            // ... other providers
        }
    }
}

// Example of use
async fn execute_trade(tx: Transaction, config: &Config) -> Result<()> {
    let signer = WalletProvider::from_config(&config.wallets)?;
    let signed_tx = signer.sign_transaction(tx).await?;
    broadcast(signed_tx).await
}
