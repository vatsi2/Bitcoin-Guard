use bitcoin::secp256k1::{Secp256k1, SecretKey};
use bitcoin::util::bip32::{ExtendedPrivKey, DerivationPath};
use bitcoin::Address;

fn generate_multisig_address(
    keys: &[ExtendedPrivKey], 
    threshold: usize
) -> Address {
    let secp = Secp256k1::new();
    let pubkeys = keys.iter()
        .map(|k| k.derive_pub(&secp, &DerivationPath::default()).unwrap())
        .collect::<Vec<_>>();

    bitcoin::Address::p2wsh(
        &bitcoin::Script::new_multisig(threshold as u32, pubkeys).unwrap(),
        bitcoin::Network::Bitcoin
    )
}
