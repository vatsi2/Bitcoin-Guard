use reqwest::Proxy;

async fn fetch_via_tor(url: &str) -> Result<String, reqwest::Error> {
    let client = reqwest::Client::builder()
        .proxy(Proxy::all("socks5h://127.0.0.1:9050")?)
        .build()?;
    Ok(client.get(url).send().await?.text().await?)
}
