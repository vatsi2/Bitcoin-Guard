use ethers::prelude::*;

pub async fn send_private_transaction(
    tx: TransactionRequest,
    provider: Provider<Http>,
    flashbots_relay: &str
) -> Result<TransactionReceipt> {
    let relay_url = Url::parse(flashbots_relay)?;
    let client = Client::new(provider, relay_url);
    let pending_tx = client.send_transaction(tx, None).await?;
    Ok(pending_tx.await?)
}
