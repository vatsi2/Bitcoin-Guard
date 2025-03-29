use aes_gcm::{Aes256Gcm, KeyInit, aead::{Aead, OsRng}};
use aes_gcm::aead::generic_array::GenericArray;

fn encrypt_key(plaintext: &[u8], password: &str) -> Vec<u8> {
    let key = GenericArray::from_slice(password.as_bytes());
    let cipher = Aes256Gcm::new(key);
    let nonce = Aes256Gcm::generate_nonce(&mut OsRng);
    cipher.encrypt(&nonce, plaintext).unwrap()
}
