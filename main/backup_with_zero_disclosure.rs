use rand::RngCore;
use std::fs::File;
use std::io::Write;

fn create_encrypted_backup(data: &[u8], path: &str) {
    let mut iv = [0u8; 12];
    rand::thread_rng().fill_bytes(&mut iv);
    let mut file = File::create(path).unwrap();
    file.write_all(&iv).unwrap();
    file.write_all(&encrypt(data, &iv)).unwrap();
}
