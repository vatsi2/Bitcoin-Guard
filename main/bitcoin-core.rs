use bitcoin::blockdata::transaction::Transaction;
use bitcoin::consensus::Decodable;

fn parse_raw_tx(raw_hex: &str) -> Result<Transaction, Box<dyn std::error::Error>> {
    let bytes = hex::decode(raw_hex)?;
    let mut decoder = std::io::Cursor::new(bytes);
    Ok(Transaction::consensus_decode(&mut decoder)?)
}
