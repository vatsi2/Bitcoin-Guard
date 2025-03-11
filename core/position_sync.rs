pub async fn sync_positions_across_protocols(&self) {
    let protocols = vec!["Aave", "Compound", "Maker", "Lido"];
    let mut aggregated_positions = Vec::new();
    
    for protocol in protocols {
        let positions = self.fetch_protocol_positions(protocol).await;
        aggregated_positions.extend(positions);
    }
    
    self.calculate_cross_protocol_health(aggregated_positions);
}
