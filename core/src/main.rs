#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let config = Config::load("whale_flow.toml")?;
    let engine = TradingEngine::new(config).await?;
    engine.run().await
}
