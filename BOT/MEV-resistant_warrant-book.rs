impl MevShield {
    pub fn bundle_transactions(txs: Vec<Transaction>, strategy: ExecutionStrategy) -> ProtectedBundle {
        let mut bundle = Bundle::new(txs);
        bundle.apply_strategy(strategy);
        bundle.sign_with_attestation(ATTESTATION_KEY);
        bundle.seal()
    }
}
