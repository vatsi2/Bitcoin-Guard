fn stock_to_flow_model(btc_supply: f64, annual_production: f64) -> f64 {
    (btc_supply / annual_production) * 100.0 // Simplified version
}
