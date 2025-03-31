use bitcoin::secp256k1::{Secp256k1, KeyPair};
use bitcoin::util::psbt::PartiallySignedTransaction;

struct MultiSigVault {
    keys: Vec<KeyPair>,
    required_sigs: usize,
}

impl MultiSigVault {
    fn sign_transaction(&self, psbt: &mut PartiallySignedTransaction) {
        let secp = Secp256k1::new();
        // Requires 3 signatures out of 5 keys
        for key in &self.keys[..3] {
            psbt.sign(key, &secp).unwrap();
        }
    }
}
