// src/compliance/mod.rs
use std::collections::HashSet;

pub struct ComplianceChecker {
    blocked_addresses: HashSet<String>,
}

impl ComplianceChecker {
    pub async fn update_sanctions_list(&mut self) {
        let response = reqwest::get("https://api.treasury.gov/sdn")
            .await
            .unwrap()
            .text()
            .await
            .unwrap();
        
        self.blocked_addresses = response.lines().collect();
    }

    pub fn is_blocked(&self, address: &str) -> bool {
        self.blocked_addresses.contains(address)
    }
}
