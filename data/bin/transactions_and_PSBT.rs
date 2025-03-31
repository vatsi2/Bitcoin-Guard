// src/transaction/mod.rs
use bitcoin::{psbt::PartiallySignedTransaction, Transaction, Script};

pub struct TransactionBuilder {
    psbt: PartiallySignedTransaction,
    inputs: Vec<Transaction>,
}

impl TransactionBuilder {
    pub fn new(inputs: Vec<Transaction>, outputs: Vec<(Script, u64)>) -> Self {
        let mut psbt = PartiallySignedTransaction::from_unsigned_tx(tx);
        // Инициализация PSBT
        Self { psbt, inputs }
    }

    pub fn add_signature(&mut self, pubkey: &ExtendedPubKey, signature: Vec<u8>) {
        // Логика добавления подписи
    }

    pub fn finalize(self) -> Result<Transaction, TransactionError> {
        // Финализация транзакции
    }
}
