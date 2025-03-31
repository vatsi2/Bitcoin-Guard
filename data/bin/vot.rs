use bitcoin::consensus::encode::deserialize;
use bitcoin::Transaction;

fn verify_tx(raw_tx: &[u8]) -> bool {
    let tx: Transaction = deserialize(raw_tx).unwrap();
    tx.is_coin_base() // Example of verification
}
