// src/blockchain/bitcoin.rs
use reqwest::Client;
use serde_json::json;

pub struct BitcoinNodeClient {
    client: Client,
    rpc_url: String,
    auth: String,
}

impl BitcoinNodeClient {
    pub async fn get_utxos(&self, address: &str) -> Result<Vec<Utxo>, NodeError> {
        let payload = json!({
            "jsonrpc": "2.0",
            "method": "listunspent",
            "params": [0, 9999999, [address]],
        });
        
        let res = self.client.post(&self.rpc_url)
            .basic_auth("user", Some("pass"))
            .json(&payload)
            .send()
            .await?;
        
        res.json::<Vec<Utxo>>().await
    }
}
