use aes_gcm::{Aes256Gcm, KeyInit, aead::{Aead, OsRng}};

fn encrypt_vault(data: &[u8]) -> Vec<u8> {
    let key = Aes256Gcm::generate_key(&mut OsRng);
    let cipher = Aes256Gcm::new(&key);
    let nonce = aes_gcm::Nonce::from_slice(b"unique_nonce");
    cipher.encrypt(nonce, data).unwrap()
}
