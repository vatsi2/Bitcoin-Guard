use chainlink::ChainlinkClient;

pub struct PriceFeedAggregator {
    pub chainlink: ChainlinkClient,
    pub pyth: PythClient,
}

impl PriceFeedAggregator {
    pub async fn get_robust_price(&self, pair: &str) -> f64 {
        let cl_price = self.chainlink.get_price(pair).await;
        let pyth_price = self.pyth.get_price(pair).await;
        (cl_price + pyth_price) / 2.0
    }
}
