pub async fn optimize_collateral_ratios(&mut self, target_safety_margin: f64) {
    let total_value = self.calculate_total_portfolio_value().await;
    for position in &mut self.positions {
        let required_collateral = position.debt * target_safety_margin;
        if position.collateral_value < required_collateral {
            self.rebalance_from_reserves(position, required_collateral).await;
        }
    }
}
