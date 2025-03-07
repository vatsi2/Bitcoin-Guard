async fn execute_rwa_arbitrage(asset: RwaAsset, chains: [Chain; 2]) -> Result<TransactionBatch> {
    let prices = fetch_prices(&asset, chains).await?;
    if let Some(profit) = calculate_profit(prices, FEE_MODEL) {
        let txs = prepare_crosschain_swap(asset, profit.threshold).await?;
        sign_and_broadcast(txs, MULTISIG_CONFIG).await
    } else {
        Err(ArbitrageError::NoOpportunity)
    }
}
