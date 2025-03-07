// src/arbitrage/rwa_arbitrage.rs

#[derive(Encode, Decode, Clone, Debug, TypeInfo)]
pub struct RwaArbitrageOpportunity {
    pub source_chain: ChainId,
    pub target_chain: ChainId,
    pub asset: AssetId,
    pub spread_percent: FixedU128,
}

#[transactional]
pub async fn find_rwa_arbitrage(
    ctx: Context,
    min_profit: Balance,
) -> Result<Vec<RwaArbitrageOpportunity>, Error> {
    let prices = ctx.oracle.get_prices(OracleSource::Pyth).await?;
    
    opportunities.into_iter()
        .filter(|opp| {
            // Фильтр: 5% спред + комиссии моста
            opp.spread_percent > FixedU128::from_float(0.05) 
                && opp.asset.risk_level < RiskLevel::Medium
        })
        .collect()
}

pub async fn execute_arbitrage(
    opportunity: RwaArbitrageOpportunity,
    vault: &MultiSigVault,
) -> Result<TransactionBatchId> {
    let bridge_tx = AxelarBridge::prepare_transfer(
        opportunity.asset, 
        opportunity.source_chain, 
        opportunity.target_chain
    ).await?;

    let swap_tx = DexAggregator::best_price_swap(
        opportunity.asset,
        Asset::USDC,
        opportunity.amount,
        Slippage::from_percent(0.5)
    ).await?;

    let bundle = MevShield::bundle_transactions(vec![bridge_tx, swap_tx])
        .with_priority(FeePriority::High)
        .seal();

    vault.sign_and_broadcast(bundle).await
}
