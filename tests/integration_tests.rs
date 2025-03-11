#[cfg(test)]
mod tests {
    #[tokio::test]
    async fn test_liquidation_protection() {
        let shield = LiquidationShield::new("0x...");
        shield.check_position();
        // Assert collateral adjustment
    }
}
