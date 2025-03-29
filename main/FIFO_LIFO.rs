use csv::Reader;
use serde::Deserialize;

#[derive(Debug, Deserialize)]
struct TransactionRecord {
    timestamp: u64,
    amount: f64,
    price: f64,
}

fn calculate_fifo(records: Vec<TransactionRecord>) -> f64 {
    let mut sorted = records.clone();
    sorted.sort_by(|a, b| a.timestamp.cmp(&b.timestamp));
    // FIFO implementation
}
