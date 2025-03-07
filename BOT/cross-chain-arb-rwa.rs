async fn execute_rwa_arbitrage(asset: RwaAsset, chains: [Chain; 2]) -> Result<TransactionBatch> {
    let prices = fetch_prices(&asset, chains).await?;
    if let Some(profit) = calculate_profit(prices, FEE_MODEL) {
        let txs = prepare_crosschain_swap(asset, profit.threshold).await?;
        sign_and_broadcast(txs, MULTISIG_CONFIG).await
    } else {
        Err(ArbitrageError::NoOpportunity)
    }
}
async fn execute_arbitrage(asset: RwaAsset) -> Result<()> {
    let eth_price = get_price(asset, Chain::Ethereum).await?;
    let cosmos_price = get_price(asset, Chain::Cosmos).await?;
    if eth_price > cosmos_price * 1.05 { // Порог 5%
        bridge_asset(asset, Cosmos => Ethereum).await?;
        sell_on_dex(asset, Ethereum).await?;
    }
    Ok(())
}
