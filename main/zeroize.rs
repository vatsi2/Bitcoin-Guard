use zeroize::Zeroize;

struct SensitiveData {
    private_key: Vec<u8>,
    seed_phrase: String,
}

impl Drop for SensitiveData {
    fn drop(&mut self) {
        self.private_key.zeroize();
        self.seed_phrase.zeroize();
    }
}
