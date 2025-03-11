use binance_rs::{websocket::BinanceWebSocket, Client};

pub struct BinancePrivateAPI {
    client: Client,
    ws: BinanceWebSocket,
}

impl BinancePrivateAPI {
    pub async fn new(api_key: &str, secret: &str) -> Self {
        let client = Client::new(api_key, secret);
        let ws = BinanceWebSocket::connect("wss://stream.binance.com:9443").await;
        Self { client, ws }
    }
}
