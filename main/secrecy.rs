use secrecy::{Secret, Zeroize};
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize, Zeroize)]
#[zeroize(drop)]
struct ApiKey {
    #[serde(skip_serializing)]
    key: Secret<String>,
    exchange: String,
}

impl ApiKey {
    pub fn new(key: String, exchange: &str) -> Self {
        Self {
            key: Secret::new(key),
            exchange: exchange.to_string(),
        }
    }
}
