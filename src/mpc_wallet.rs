use arkworks::mpc::threshold_signature;

pub struct MPCWallet {
    pub participants: Vec<Participant>,
    pub threshold: u8,
}

impl MPCWallet {
    pub fn sign_transaction(&self, tx: Transaction) -> Result<Signature> {
        let shares = self.participants
            .iter()
            .map(|p| p.generate_share(&tx))
            .collect::<Result<Vec<_>>>()?;
        
        threshold_signature::combine(shares, self.threshold)
    }
}
