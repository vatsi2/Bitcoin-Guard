use arti_client::{TorClient, Config};

async fn tor_request() -> Result<String, arti_client::Error> {
    let config = Config::default();
    let tor_client = TorClient::create_bootstrapped(config).await?;
    tor_client.get("http://example.com").await?.text().await
}
