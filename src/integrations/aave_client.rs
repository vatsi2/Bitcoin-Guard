use ethers_contract::abigen;

abigen!(
    AaveLendingPool,
    "abis/aave_v3/LendingPool.json",
    event_derives(serde::Deserialize, serde::Serialize)
);

pub struct AaveClient {
    pub contract: AaveLendingPool<Provider<Http>>,
}

impl AaveClient {
    pub async fn get_user_account_data(&self, user: Address) -> Result<UserAccountData> {
        self.contract.get_user_account_data(user).call().await
    }
}
