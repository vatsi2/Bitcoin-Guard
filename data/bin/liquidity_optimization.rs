fn calculate_order_sizes(total: f64, volatility: f64) -> Vec<f64> {
    let chunks = (total / (volatility * 0.1)) as usize;
    vec![total / chunks as f64; chunks]
}
