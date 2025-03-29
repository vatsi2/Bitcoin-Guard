use bitcoin::util::sighash::SighashCache;
use bitcoin::{Script, Transaction};

fn verify_signature(
    tx: &Transaction,
    input_index: usize,
    script: &Script,
    value: u64,
    pubkey: &PublicKey,
    signature: &Signature,
) -> bool {
    let mut cache = SighashCache::new(tx);
    let sighash = cache.segwit_signature_hash(input_index, script, value, SigHashType::All);
    secp.verify(&sighash.to_msg(), signature, pubkey).is_ok()
}
