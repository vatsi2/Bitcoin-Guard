// tests/arbitrage_engine_test.rs

#[tokio::test]
async fn test_rwa_arbitrage_flow() {
    let mock_oracle = MockOracle::new()
        .set_price("Ondo", 105.0, Chain::Ethereum)
        .set_price("Ondo", 100.0, Chain::Cosmos);
    
    let engine = ArbitrageEngine::new(mock_oracle);
    let opportunities = engine.find_opportunities().await.unwrap();
    
    assert!(!opportunities.is_empty());
    let best = opportunities.first().unwrap();
    
    assert_eq!(best.spread_percent, 0.05); // 5% spread
    assert_eq!(best.source_chain, Chain::Cosmos);
    assert_eq!(best.target_chain, Chain::Ethereum);
}
