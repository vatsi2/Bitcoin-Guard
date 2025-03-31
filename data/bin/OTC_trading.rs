use reqwest::Client;
use std::time::Duration;

struct OTCTrader {
    client: Client,
    daily_limit: f64,
}

impl OTCTrader {
    async fn sell_btc(&self, amount: f64) -> Result<(), reqwest::Error> {
        if amount > self.daily_limit {
            panic!("Daily limit exceeded!");
        }
        self.client.post("https://api.binance.com/otc")
            .body(format!("amount={}", amount))
            .send().await?;
        Ok(())
    }
}
