struct Transaction {
    amount: f64,
    price: f64,
    timestamp: i64,
}

fn calculate_hifo(txs: Vec<Transaction>) -> Vec<Transaction> {
    let mut sorted = txs.clone();
    sorted.sort_by(|a, b| b.price.partial_cmp(&a.price).unwrap());
    sorted
}
