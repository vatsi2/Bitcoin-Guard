enum TaxMethod { FIFO, LIFO, HIFO }

fn simulate_taxes(method: TaxMethod, txs: Vec<Transaction>) -> f64 {
    match method {
        TaxMethod::HIFO => calculate_hifo(txs).iter().map(|t| t.amount).sum(),
        // ... другие методы
    }
}
