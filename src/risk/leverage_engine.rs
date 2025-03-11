pub struct LeverageCalculator {
    pub volatility: f64,
    pub correlation_matrix: HashMap<String, f64>,
}

impl LeverageCalculator {
    pub fn optimal_leverage(&self, asset: &str) -> f64 {
        let max_leverage = 1.0 / (self.volatility * 2.0);
        max_leverage.min(10.0) // Cap at 10x
    }
}
