use ethers::middleware::SignerMiddleware;
use flashbots::FlashbotsMiddleware;

pub async fn create_mev_protected_client(
    provider: Provider<Http>,
    signer: LocalWallet,
) -> Result<SignerMiddleware<FlashbotsMiddleware<Provider<Http>>, LocalWallet>> {
    let flashbots_middleware = FlashbotsMiddleware::new(
        provider,
        Url::parse("https://relay.flashbots.net")?,
        signer.clone(),
    );
    
    Ok(SignerMiddleware::new(flashbots_middleware, signer))
}
